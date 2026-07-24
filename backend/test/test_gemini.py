from app.services.gemini_service import GeminiService

service = GeminiService()

answer = service.ask(
    "Why is my cloud cost increasing?"
)

print(answer)