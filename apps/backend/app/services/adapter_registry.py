from app.adapters.base import DeviceAdapter
from app.adapters.blood_pressure_monitor import BloodPressureAdapter
from app.models.unified import SourceType


class AdapterRegistry:
    def __init__(self) -> None:
        default_adapter = BloodPressureAdapter()
        self._adapters: dict[SourceType, DeviceAdapter] = {
            SourceType.IOT: default_adapter,
            SourceType.BLUETOOTH: default_adapter,
            SourceType.MANUAL: default_adapter,
            SourceType.IMPORT: default_adapter,
            SourceType.EXTERNAL: default_adapter,
        }

    def get(self, source_type: SourceType) -> DeviceAdapter:
        return self._adapters[source_type]
