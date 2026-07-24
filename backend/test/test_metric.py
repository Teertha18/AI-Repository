from app.services.metrics_service import MetricsService

print(
    MetricsService().get_dashboard_metrics()
)