from fastapi import APIRouter

from app.services.forecast_service import ForecastService

router = APIRouter(prefix="/forecast", tags=["Forecast"])


@router.get("/{service}")
def get_forecast(service: str):

    forecast = ForecastService()

    return {
        "status": "success",
        "message": "Forecast generated successfully.",
        "data": forecast.get_forecast(service)
    }