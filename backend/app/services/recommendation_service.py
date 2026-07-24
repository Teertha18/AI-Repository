"""
Recommendation Service
"""

from app.engines.recommendation_engine import RecommendationEngine
from app.services.forecast_service import ForecastService
from app.providers.provider_factory import ProviderFactory


class RecommendationService:

    def __init__(self):

        self.provider = ProviderFactory.get_provider()
        self.forecast = ForecastService()

    def get_recommendations(self):

        services = [
            "bigquery",
            "dataproc",
            "dataflow",
            "gcs"
        ]

        results = []

        total_savings = 0

        for service in services:

            forecast = self.forecast.get_forecast(service)

            current = forecast["current_value"]

            predicted = forecast["forecast"][-1]["value"]

            recommendations = RecommendationEngine.analyze(
                service,
                current,
                predicted
            )

            for recommendation in recommendations:

                total_savings += recommendation["estimated_savings"]

                recommendation["service"] = service

                results.append(recommendation)

        return {
            "total_recommendations": len(results),
            "estimated_monthly_savings": total_savings,
            "recommendations": results
        }