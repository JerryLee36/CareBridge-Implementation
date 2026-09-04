from datetime import datetime, timezone

from app.ingestion.schemas import RawDevicePayload
from app.models.unified import DomainType, SourceType
from app.services.pipeline import IngestionPipeline


def test_alert_and_task_are_generated_for_high_bp():
    payload = RawDevicePayload(
        message_id="evt-1",
        person_id="person-1",
        source_type=SourceType.IOT,
        source_device_id="bp-001",
        metric="systolic_bp",
        value=168,
        unit="mmHg",
        occurred_at=datetime.now(timezone.utc),
        domain=DomainType.VITAL,
    )

    result = IngestionPipeline().run(payload)

    assert result["observation"].person_id == "person-1"
    assert result["alert"] is not None
    assert result["task"] is not None
