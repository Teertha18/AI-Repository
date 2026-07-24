"""
Dashboard Models
"""

from pydantic import BaseModel


class DashboardSummary(BaseModel):
    total_cost: float
    cpu: float
    memory: float
    storage: float
    carbon_score: int
    optimization_score: int


class CostHistory(BaseModel):
    date: str
    cost: float


class DashboardResponse(BaseModel):
    summary: DashboardSummary
    history: list[CostHistory]
    recommendations: list[str]