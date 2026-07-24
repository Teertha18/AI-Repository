from fastapi import APIRouter

from app.models.response import ApiResponse
from app.core.config import settings

router = APIRouter(tags=["Health"])


@router.get("/health", response_model=ApiResponse)
def health():

    return ApiResponse(
        status="success",
        message="Service is healthy.",
        data={
            "application": settings.APP_NAME,
            "version": settings.VERSION,
            "status": "Running"
        }
    )