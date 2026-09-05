from app.models.platform import AuditLogEntry, UserRole


class AuditLogService:
    def __init__(self) -> None:
        self._entries: list[AuditLogEntry] = []

    def record(self, action: str, actor_role: UserRole, resource_type: str, resource_id: str) -> AuditLogEntry:
        entry = AuditLogEntry(
            action=action,
            actor_role=actor_role,
            resource_type=resource_type,
            resource_id=resource_id,
        )
        self._entries.append(entry)
        return entry

    def list_entries(self) -> list[AuditLogEntry]:
        return self._entries
