from app.ai.context_builder import ContextBuilder
from app.services.gemini_service import GeminiService


class AIAnalysisService:

    def __init__(self):

        self.gemini = GeminiService()

    def analyze(self):

        context = ContextBuilder.build()

        return self.gemini.ask(context)