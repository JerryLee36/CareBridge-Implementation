from app.models.platform import UserRole


class RBACService:
    def __init__(self) -> None:
        self._role_permissions: dict[UserRole, set[str]] = {
            UserRole.ADMIN: {
                "dashboard:read",
                "users:manage",
                "devices:manage",
                "settings:manage",
                "rules:manage",
            },
            UserRole.CAREGIVER: {"tasks:read", "tasks:update", "handover:write"},
            UserRole.CLINICIAN: {"reports:read", "advice:write", "risk:read"},
            UserRole.FAMILY: {"reports:read", "alerts:read", "feedback:write"},
        }

    def has_permission(self, role: UserRole, permission: str) -> bool:
        return permission in self._role_permissions.get(role, set())

    def list_permissions(self, role: UserRole) -> list[str]:
        return sorted(self._role_permissions.get(role, set()))
