"""
Recommendation Models
"""

from pydantic import BaseModel


class Recommendation(BaseModel):
    severity: str
    category: str
    title: str
    description: str
    estimated_savings: float


class RecommendationResponse(BaseModel):
    recommendations: list[Recommendation]