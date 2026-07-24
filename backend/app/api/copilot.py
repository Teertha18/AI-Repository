from fastapi import APIRouter

from app.models.copilot import CopilotRequest
from app.models.response import ApiResponse
from app.services.copilot_service import CopilotService

router = APIRouter(tags=["Copilot"])


@router.post("/copilot/ask", response_model=ApiResponse)
def ask_copilot(request: CopilotRequest):

    service = CopilotService()

    result = service.ask(request.question)

    return ApiResponse(
        status="success",
        message="AI response generated successfully.",
        data=result
    )