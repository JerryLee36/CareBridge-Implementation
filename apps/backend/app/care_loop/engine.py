from datetime import datetime, timezone
from enum import Enum

from pydantic import BaseModel

from app.models.unified import UnifiedObservation
from app.rules.engine import RuleResult


class AlertStatus(str, Enum):
    OPEN = "open"
    CLOSED = "closed"


class TaskStatus(str, Enum):
    TODO = "todo"
    DONE = "done"


class Alert(BaseModel):
    alert_id: str
    person_id: str
    observation_id: str
    level: str
    reason: str
    status: AlertStatus = AlertStatus.OPEN
    created_at: datetime = datetime.now(timezone.utc)


class CareTask(BaseModel):
    task_id: str
    alert_id: str
    assignee_role: str
    title: str
    status: TaskStatus = TaskStatus.TODO
    created_at: datetime = datetime.now(timezone.utc)


class ClosedLoopEngine:
    def create_alert(self, observation: UnifiedObservation, rule: RuleResult) -> Alert:
        return Alert(
            alert_id=f"alert-{observation.observation_id}",
            person_id=observation.person_id,
            observation_id=observation.observation_id,
            level=rule.level or "medium",
            reason=rule.reason or "Rule triggered",
        )

    def dispatch_task(self, alert: Alert) -> CareTask:
        assignee_role = "nurse" if alert.level in {"high", "critical"} else "caregiver"
        return CareTask(
            task_id=f"task-{alert.alert_id}",
            alert_id=alert.alert_id,
            assignee_role=assignee_role,
            title=f"Follow up alert: {alert.reason}",
        )
