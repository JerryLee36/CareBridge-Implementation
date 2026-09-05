from app.models.platform import RuleSetVersion


class RuleRegistryService:
    def __init__(self) -> None:
        self._versions: list[RuleSetVersion] = [
            RuleSetVersion(version="v1.0", description="Baseline threshold rules"),
            RuleSetVersion(version="v1.1", description="Adds trend sensitivity adjustments", enabled=False),
        ]

    def list_versions(self) -> list[RuleSetVersion]:
        return self._versions

    def get_active_version(self) -> RuleSetVersion:
        for version in self._versions:
            if version.enabled:
                return version
        return self._versions[0]
