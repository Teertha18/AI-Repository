from fastapi import APIRouter

from app.services.ai_analysis_service import AIAnalysisService

router = APIRouter(
    prefix="/analysis",
    tags=["AI Analysis"]
)


@router.get("/")
def analyze():

    service = AIAnalysisService()

    return {
        "status": "success",
        "message": "AI analysis completed.",
        "data": service.analyze()
    }