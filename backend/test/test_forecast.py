from app.services.forecast_service import ForecastService

service = ForecastService()

print(service.get_forecast("bigquery"))

# print(service.get_forecast("dataproc"))

# print(service.get_forecast("dataflow"))

# print(service.get_forecast("gcs"))