from app.models.platform import PlatformSetting


class SystemConfigService:
    def __init__(self) -> None:
        self._settings: dict[str, PlatformSetting] = {
            "notification.default_channel": PlatformSetting(
                key="notification.default_channel",
                value="sms",
                description="Default outbound channel for routine notifications",
            ),
            "ai.assistant.enabled": PlatformSetting(
                key="ai.assistant.enabled",
                value="true",
                description="Enable AI-assisted care recommendation generation",
            ),
        }

    def list_settings(self) -> list[PlatformSetting]:
        return list(self._settings.values())

    def get_setting(self, key: str) -> PlatformSetting | None:
        return self._settings.get(key)
