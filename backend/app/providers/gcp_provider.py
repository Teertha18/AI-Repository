"""
Google Cloud Provider
"""

import os

from app.core.config import settings
from app.providers.base_provider import BaseProvider


class GCPProvider(BaseProvider):

    def __init__(self):

        if settings.google_application_credentials:
            os.environ[
                "GOOGLE_APPLICATION_CREDENTIALS"
            ] = settings.google_application_credentials

        self.project_id = settings.gcp_project_id
        self.region = settings.gcp_region

    def get_latest_metrics(self):
        """
        Returns latest utilization metrics.

        TODO:
        Cloud Monitoring integration.
        """
        return {
            "cost": 0,
            "cpu": 0,
            "memory": 0,
            "storage": 0
        }

    def get_cost_history(self):
        """
        TODO:
        BigQuery Billing Export.
        """
        return []

    def get_vm_instances(self):
        """
        TODO:
        Compute Engine.
        """
        return []

    def get_storage(self):
        """
        TODO:
        Cloud Storage.
        """
        return []

    def get_forecast_data(self):
        """
        Future ML Forecast.
        """
        return []