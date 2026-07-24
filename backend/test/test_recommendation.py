from app.services.recommendation_service import RecommendationService

service = RecommendationService()

print(service.get_recommendations())