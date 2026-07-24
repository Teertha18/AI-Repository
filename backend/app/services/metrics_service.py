from app.providers.provider_factory import ProviderFactory


class MetricsService:

    def __init__(self):
        self.provider = ProviderFactory.get_provider()

    def get_metrics(self):

        # BigQuery
        bq = self.provider.get_bigquery_usage()

        reserved = int(bq["reserved_slots"].iloc[-1])
        used = int(bq["used_slots"].iloc[-1])

        # Dataproc
        dp = self.provider.get_dataproc_usage()

        clusters = int(dp["clusters"].iloc[-1])
        active = int(dp["active_clusters"].iloc[-1])

        # Dataflow
        df = self.provider.get_dataflow_usage()

        workers = int(df["used_workers"].iloc[-1])
        max_workers = int(df["max_workers"].iloc[-1])

        # GCS
        gcs = self.provider.get_gcs_usage()

        storage = float(gcs["storage_tb"].iloc[-1])
        previous = float(gcs["storage_tb"].iloc[-2])

        growth = round(
            ((storage - previous) / previous) * 100,
            2,
        )

        return {
            "bigquery": {
                "reserved_slots": reserved,
                "used_slots": used,
                "utilization": round((used / reserved) * 100, 2),
            },
            "dataproc": {
                "clusters": clusters,
                "active_clusters": active,
                "utilization": round((active / clusters) * 100, 2),
            },
            "dataflow": {
                "used_workers": workers,
                "max_workers": max_workers,
                "utilization": round(
                    (workers / max_workers) * 100,
                    2,
                ),
            },
            "gcs": {
                "storage_tb": storage,
                "growth_percentage": growth,
            },
        }