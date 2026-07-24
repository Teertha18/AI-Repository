from fastapi import APIRouter

from app.services.recommendation_service import RecommendationService

router = APIRouter(
    prefix="/recommendations",
    tags=["Recommendations"]
)


@router.get("/")
def get_recommendations():

    service = RecommendationService()

    return {
        "status": "success",
        "message": "Recommendations generated successfully.",
        "data": service.get_recommendations()
    }