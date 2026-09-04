from app.ingestion.schemas import RawDevicePayload
from app.models.unified import UnifiedObservation


class DeviceAdapter:
    def transform(self, raw: RawDevicePayload) -> UnifiedObservation:
        raise NotImplementedError
