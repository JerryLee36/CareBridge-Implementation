from datetime import datetime, timezone
from enum import Enum

from pydantic import BaseModel, Field


class UserRole(str, Enum):
    ADMIN = "admin"
    CAREGIVER = "caregiver"
    CLINICIAN = "clinician"
    FAMILY = "family"


class NotificationChannel(str, Enum):
    SMS = "sms"
    PHONE_CALL = "phone_call"
    WECHAT = "wechat"
    EMAIL = "email"


class DataQualityReport(BaseModel):
    total_events: int
    missing_value_events: int
    duplicate_events: int
    abnormal_value_events: int
    quality_score: float


class RuleSetVersion(BaseModel):
    version: str
    description: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    enabled: bool = True


class TrendInsight(BaseModel):
    person_id: str
    metric: str
    period: str
    min_value: float
    max_value: float
    avg_value: float
    sample_count: int


class NotificationMessage(BaseModel):
    message_id: str
    person_id: str
    recipient_role: UserRole
    channel: NotificationChannel
    title: str
    body: str
    sent_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class AuditLogEntry(BaseModel):
    action: str
    actor_role: UserRole
    resource_type: str
    resource_id: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class PlatformSetting(BaseModel):
    key: str
    value: str
    description: str
