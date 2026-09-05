from datetime import datetime, timezone

from fastapi.testclient import TestClient

from app.main import app
from app.models.platform import NotificationChannel, UserRole
from app.models.unified import DomainType, SourceType, UnifiedObservation
from app.services.data_quality import DataQualityService
from app.services.notification import NotificationService
from app.services.rbac import RBACService
from app.services.trend_analysis import TrendAnalysisService


def test_data_quality_evaluates_issues():
    service = DataQualityService()
    now = datetime.now(timezone.utc)
    observations = [
        UnifiedObservation(
            observation_id="obs-1",
            person_id="p-1",
            metric="systolic_bp",
            value=160,
            unit="mmHg",
            occurred_at=now,
            source_type=SourceType.IOT,
            source_device_id="dev-1",
            domain=DomainType.VITAL,
        ),
        UnifiedObservation(
            observation_id="obs-1",
            person_id="p-1",
            metric="systolic_bp",
            value=-1,
            unit="mmHg",
            occurred_at=now,
            source_type=SourceType.IOT,
            source_device_id="dev-1",
            domain=DomainType.VITAL,
        ),
    ]

    report = service.evaluate(observations)

    assert report.total_events == 2
    assert report.duplicate_events == 1
    assert report.abnormal_value_events == 1
    assert report.quality_score < 100


def test_trend_analysis_returns_average():
    service = TrendAnalysisService()
    now = datetime.now(timezone.utc)
    observations = [
        UnifiedObservation(
            observation_id="obs-10",
            person_id="p-2",
            metric="spo2",
            value=92,
            occurred_at=now,
            source_type=SourceType.BLUETOOTH,
            source_device_id="dev-2",
            domain=DomainType.VITAL,
        ),
        UnifiedObservation(
            observation_id="obs-11",
            person_id="p-2",
            metric="spo2",
            value=96,
            occurred_at=now,
            source_type=SourceType.BLUETOOTH,
            source_device_id="dev-2",
            domain=DomainType.VITAL,
        ),
    ]

    insight = service.summarize(person_id="p-2", metric="spo2", observations=observations)

    assert insight.sample_count == 2
    assert insight.avg_value == 94.0


def test_rbac_and_notification_services_work():
    rbac = RBACService()
    notifications = NotificationService()

    assert rbac.has_permission(UserRole.ADMIN, "settings:manage")
    assert not rbac.has_permission(UserRole.FAMILY, "settings:manage")

    message = notifications.send(
        person_id="person-1",
        recipient_role=UserRole.FAMILY,
        channel=NotificationChannel.EMAIL,
        title="Weekly Summary",
        body="All key indicators are stable.",
    )

    assert message.channel == NotificationChannel.EMAIL
    assert len(notifications.list_messages()) == 1


def test_role_based_routes_return_expected_payloads():
    client = TestClient(app)

    response = client.post(
        "/ingestion/events",
        json={
            "message_id": "evt-role-1",
            "person_id": "person-route-1",
            "source_type": "iot",
            "source_device_id": "dev-route",
            "metric": "systolic_bp",
            "value": 170,
            "unit": "mmHg",
            "occurred_at": datetime.now(timezone.utc).isoformat(),
            "domain": "vital",
        },
    )
    assert response.status_code == 200

    admin = client.get("/admin/dashboard")
    caregiver = client.get("/caregiver/tasks/today")
    clinician = client.get("/clinician/trend/person-route-1/systolic_bp")
    family = client.get("/family/reports/person-route-1")

    assert admin.status_code == 200
    assert caregiver.status_code == 200
    assert clinician.status_code == 200
    assert family.status_code == 200
    assert admin.json()["overview"]["total_observations"] >= 1
    assert clinician.json()["sample_count"] >= 1
