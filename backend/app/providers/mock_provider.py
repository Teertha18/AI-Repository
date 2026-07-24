"""
Mock Provider

Provides mock data for:

- BigQuery
- Dataproc
- Dataflow
- GCS

Later this provider will be replaced by GCPProvider.
"""

from pathlib import Path

import pandas as pd

from app.providers.base_provider import BaseProvider


class MockProvider(BaseProvider):

    def __init__(self):

        self.data_path = (
            Path(__file__)
            .resolve()
            .parents[2]
            / "mock_data"
        )

    def _load_csv(self, filename: str):

        return pd.read_csv(
            self.data_path / filename
        )

    # ------------------------
    # BigQuery
    # ------------------------

    def get_bigquery_usage(self):

        return self._load_csv(
            "bigquery_usage.csv"
        )

    # ------------------------
    # Dataproc
    # ------------------------

    def get_dataproc_usage(self):

        return self._load_csv(
            "dataproc_usage.csv"
        )

    # ------------------------
    # Dataflow
    # ------------------------

    def get_dataflow_usage(self):

        return self._load_csv(
            "dataflow_usage.csv"
        )

    # ------------------------
    # GCS
    # ------------------------

    def get_gcs_usage(self):

        return self._load_csv(
            "gcs_usage.csv"
        )