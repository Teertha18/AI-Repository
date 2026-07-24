from fastapi import APIRouter

from app.services.metrics_service import MetricsService

router = APIRouter(prefix="/metrics", tags=["Metrics"])


@router.get("/")
def get_metrics():

    service = MetricsService()

    return {
        "status": "success",
        "message": "Metrics retrieved successfully.",
        "data": service.get_metrics()
    }