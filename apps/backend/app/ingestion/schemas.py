from datetime import datetime
from pydantic import BaseModel

from app.models.unified import DomainType, SourceType


class RawDevicePayload(BaseModel):
    message_id: str
    person_id: str
    source_type: SourceType
    source_device_id: str
    metric: str
    value: float | int | str
    unit: str | None = None
    occurred_at: datetime
    domain: DomainType
