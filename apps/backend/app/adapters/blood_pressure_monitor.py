from app.adapters.base import DeviceAdapter
from app.ingestion.schemas import RawDevicePayload
from app.models.unified import UnifiedObservation


class BloodPressureAdapter(DeviceAdapter):
    """Maps source payloads into unified blood-pressure observations."""

    def transform(self, raw: RawDevicePayload) -> UnifiedObservation:
        return UnifiedObservation(
            observation_id=raw.message_id,
            person_id=raw.person_id,
            metric=raw.metric,
            value=raw.value,
            unit=raw.unit,
            occurred_at=raw.occurred_at,
            source_type=raw.source_type,
            source_device_id=raw.source_device_id,
            domain=raw.domain,
            raw_payload=raw.model_dump(),
        )
