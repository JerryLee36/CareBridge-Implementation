from fastapi import APIRouter

from app.models.platform import UserRole
from app.services.platform_context import platform_context

router = APIRouter(prefix="/caregiver", tags=["caregiver"])


@router.get("/tasks/today")
def get_todays_tasks():
    return {
        "tasks": [
            {
                "task_id": "cg-task-1",
                "title": "Check blood pressure and hydration",
                "priority": "high",
                "instruction": "Recheck in 30 minutes if systolic BP remains above 160 mmHg.",
                "status": "todo",
            }
        ]
    }


@router.post("/handover")
def submit_handover(note: str):
    log = platform_context.audit.record(
        action="handover_submitted",
        actor_role=UserRole.CAREGIVER,
        resource_type="handover_note",
        resource_id="handover-latest",
    )
    return {"status": "recorded", "note": note, "audit": log.model_dump(mode="json")}
