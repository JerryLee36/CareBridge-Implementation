from fastapi import APIRouter

from app.services.observation_store import observation_store
from app.services.platform_context import platform_context

router = APIRouter(prefix="/admin", tags=["admin"])


@router.get("/dashboard")
def admin_dashboard():
    observations = observation_store.list()
    quality = platform_context.data_quality.evaluate(observations)
    active_ruleset = platform_context.rule_registry.get_active_version()
    settings = platform_context.system_config.list_settings()

    return {
        "overview": {
            "total_observations": len(observations),
            "active_ruleset": active_ruleset.model_dump(mode="json"),
            "quality_score": quality.quality_score,
        },
        "data_quality": quality.model_dump(mode="json"),
        "system_settings": [item.model_dump(mode="json") for item in settings],
    }


@router.get("/permissions/{role}")
def role_permissions(role: str):
    from app.models.platform import UserRole

    typed_role = UserRole(role)
    return {"role": typed_role, "permissions": platform_context.rbac.list_permissions(typed_role)}
