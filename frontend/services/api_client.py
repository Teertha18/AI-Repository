"""
API Client

Handles all communication with the FastAPI backend.
"""

import requests

BASE_URL = "http://127.0.0.1:8000/api/v1"


class APIClient:

    @staticmethod
    def _get(endpoint: str):
        response = requests.get(f"{BASE_URL}/{endpoint}")
        response.raise_for_status()

        payload = response.json()

        return payload["data"]

    @staticmethod
    def get_metrics():
        return APIClient._get("metrics/")

    @staticmethod
    @staticmethod
    def get_forecast(service: str):
        return APIClient._get(f"forecast/{service}")

    @staticmethod
    def get_recommendations():
        return APIClient._get("recommendations/")

    @staticmethod
    @staticmethod
    def ask_copilot(question):

        response = requests.post(
            f"{BASE_URL}/copilot/ask",
            json={
                "question": question
            }
        )

        response.raise_for_status()

        return response.json()["data"]
    
    @staticmethod
    def get_analysis():
        return APIClient._get("analysis/")