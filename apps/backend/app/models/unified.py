from datetime import datetime, timezone
from enum import Enum
from typing import Any

from pydantic import BaseModel, Field


class SourceType(str, Enum):
    IOT = "iot"
    BLUETOOTH = "bluetooth"
    MANUAL = "manual"
    IMPORT = "import"
    EXTERNAL = "external"


class DomainType(str, Enum):
    VITAL = "vital"
    BEHAVIOR = "behavior"
    ENVIRONMENT = "environment"
    CARE_RECORD = "care_record"
    MEDICATION = "medication"
    EVENT = "event"


class UnifiedObservation(BaseModel):
    observation_id: str
    person_id: str
    metric: str
    value: float | int | str
    unit: str | None = None
    occurred_at: datetime
    recorded_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    source_type: SourceType
    source_device_id: str | None = None
    domain: DomainType
    tags: list[str] = Field(default_factory=list)
    raw_payload: dict[str, Any] = Field(default_factory=dict)


class Person(BaseModel):
    person_id: str
    name: str
    date_of_birth: str | None = None
    gender: str | None = None


class Contact(BaseModel):
    contact_id: str
    person_id: str
    relation: str
    name: str
    phone: str | None = None
