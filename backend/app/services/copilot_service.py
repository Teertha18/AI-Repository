from app.ai.context_builder import ContextBuilder
from app.ai.prompt_builder import PromptBuilder
from app.services.gemini_service import GeminiService


class CopilotService:

    def __init__(self):
        self.gemini = GeminiService()

    def ask(self, question: str):

        context = ContextBuilder.build()

        prompt = f"""
You are a Senior Google Cloud Architect.

Current Cloud Environment:

{context}

User Question:

{question}

Answer in a concise and professional manner.
"""

        return self.gemini.ask_text(prompt)