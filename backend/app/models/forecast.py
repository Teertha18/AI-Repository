"""
Forecast Response Models
"""

from pydantic import BaseModel


class ForecastSummary(BaseModel):
    current_month_cost: float
    predicted_month_cost: float
    growth_percentage: float
    confidence: int


class ForecastPoint(BaseModel):
    day: int
    cost: float


class ForecastResponse(BaseModel):
    summary: ForecastSummary
    forecast: list[ForecastPoint]