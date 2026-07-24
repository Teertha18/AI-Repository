from services.api_client import APIClient

print(APIClient.get_metrics())
print(APIClient.get_forecast())
print(APIClient.get_recommendations())
print(APIClient.ask_copilot("Why is my cloud cost increasing?"))