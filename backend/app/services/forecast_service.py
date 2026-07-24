"""
Forecast Service

Generates forecast for supported GCP services.
"""

from app.engines.forecast_engine import ForecastEngine
from app.providers.provider_factory import ProviderFactory


class ForecastService:

    def __init__(self):
        self.provider = ProviderFactory.get_provider()

    def get_forecast(self, service: str):

        mapping = {
            "bigquery": (
                self.provider.get_bigquery_usage(),
                "reserved_slots",
                "used_slots",
            ),
            "dataproc": (
                self.provider.get_dataproc_usage(),
                "clusters",
                "active_clusters",
            ),
            "dataflow": (
                self.provider.get_dataflow_usage(),
                "max_workers",
                "used_workers",
            ),
            "gcs": (
                self.provider.get_gcs_usage(),
                None,
                "storage_tb",
            ),
        }

        if service not in mapping:
            raise ValueError(f"Unsupported service: {service}")

        df, capacity_column, usage_column = mapping[service]

        predictions = ForecastEngine.predict(
            dataframe=df,
            column=usage_column,
            days=30,
        )

        current = float(df[usage_column].iloc[-1])

        forecast = [
            {
                "day": i,
                "value": round(float(value), 2),
            }
            for i, value in enumerate(predictions, start=1)
        ]

        response = {
            "service": service,
            "metric": usage_column,
            "current": current,
            "forecast": forecast,
        }

        if capacity_column:
            capacity = float(df[capacity_column].iloc[-1])

            response["capacity"] = capacity

            response["utilization"] = round(
                (current / capacity) * 100,
                2,
            )
        else:
            growth = (
                (forecast[-1]["value"] - current)
                / current
            ) * 100

            response["growth_percentage"] = round(
                growth,
                2,
            )

        return response