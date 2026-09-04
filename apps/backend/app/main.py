from fastapi import FastAPI

from app.api.routes_ingestion import router as ingestion_router
from app.core.config import settings

app = FastAPI(title=settings.app_name)
app.include_router(ingestion_router)


@app.get("/health")
def health_check():
    return {"status": "ok", "service": settings.app_name}
