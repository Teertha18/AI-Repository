"""
Context Builder

Collects cloud metrics and historical data
to build the AI context.
"""

from app.providers.provider_factory import ProviderFactory


class ContextBuilder:

    @staticmethod
    def build():

        provider = ProviderFactory.get_provider()

        # -------------------------
        # BigQuery
        # -------------------------

        bq = provider.get_bigquery_usage()

        bigquery = {
            "current": {
                "reserved_slots": int(bq["reserved_slots"].iloc[-1]),
                "used_slots": int(bq["used_slots"].iloc[-1]),
                "utilization": round(
                    (
                        bq["used_slots"].iloc[-1]
                        / bq["reserved_slots"].iloc[-1]
                    ) * 100,
                    2,
                ),
            },
            "history": bq.to_dict(orient="records"),
        }

        # -------------------------
        # Dataproc
        # -------------------------

        dp = provider.get_dataproc_usage()

        dataproc = {
            "current": {
                "clusters": int(dp["clusters"].iloc[-1]),
                "active_clusters": int(dp["active_clusters"].iloc[-1]),
            },
            "history": dp.to_dict(orient="records"),
        }

        # -------------------------
        # Dataflow
        # -------------------------

        df = provider.get_dataflow_usage()

        dataflow = {
            "current": {
                "max_workers": int(df["max_workers"].iloc[-1]),
                "used_workers": int(df["used_workers"].iloc[-1]),
                "utilization": round(
                    (
                        df["used_workers"].iloc[-1]
                        / df["max_workers"].iloc[-1]
                    ) * 100,
                    2,
                ),
            },
            "history": df.to_dict(orient="records"),
        }

        # -------------------------
        # GCS
        # -------------------------

        gcs_df = provider.get_gcs_usage()

        current_storage = float(gcs_df["storage_tb"].iloc[-1])
        previous_storage = float(gcs_df["storage_tb"].iloc[-2])

        growth = round(
            ((current_storage - previous_storage) / previous_storage) * 100,
            2,
        )

        gcs = {
            "current": {
                "storage_tb": current_storage,
                "growth_percentage": growth,
            },
            "history": gcs_df.to_dict(orient="records"),
        }

        # -------------------------
        # Final Context
        # -------------------------

        return {
            "project": "Hackathon Demo",
            "services": {
                "bigquery": bigquery,
                "dataproc": dataproc,
                "dataflow": dataflow,
                "gcs": gcs,
            },
        }