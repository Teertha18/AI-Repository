"""
Recommendation Engine

Generates optimization recommendations
based on current utilization and forecast.
"""


class RecommendationEngine:

    @staticmethod
    def analyze(service: str, current: float, predicted: float):

        recommendations = []

        if service == "bigquery":

            utilization = (current / 500) * 100

            if utilization > 90:
                recommendations.append({
                    "title": "Increase Reserved Slots",
                    "severity": "High",
                    "reason": "BigQuery slot utilization is consistently high.",
                    "estimated_savings": 0
                })

            elif utilization < 50:
                recommendations.append({
                    "title": "Reduce Reserved Slots",
                    "severity": "Medium",
                    "reason": "Reserved slots are underutilized.",
                    "estimated_savings": 250
                })

        elif service == "dataproc":

            if current >= 5:
                recommendations.append({
                    "title": "Increase Cluster Capacity",
                    "severity": "Medium",
                    "reason": "Cluster utilization is near maximum.",
                    "estimated_savings": 0
                })

        elif service == "dataflow":

            if current >= 32:
                recommendations.append({
                    "title": "Increase Worker Pool",
                    "severity": "Medium",
                    "reason": "Worker utilization is high.",
                    "estimated_savings": 0
                })

        elif service == "gcs":

            if predicted > current * 1.15:
                recommendations.append({
                    "title": "Enable Lifecycle Policies",
                    "severity": "Low",
                    "reason": "Storage growth trend detected.",
                    "estimated_savings": 180
                })

        if not recommendations:
            recommendations.append({
                "title": "No Action Required",
                "severity": "Info",
                "reason": "Current utilization is healthy.",
                "estimated_savings": 0
            })

        return recommendations