"""
Gemini Service
"""

import google.generativeai as genai
import json

from app.core.config import settings
from app.ai.context_builder import ContextBuilder
from app.ai.prompt_builder import PromptBuilder


class GeminiService:

    def __init__(self):

        genai.configure(api_key=settings.gemini_api_key)

        self.model = genai.GenerativeModel(
            settings.gemini_model
        )

    def ask(self, context: dict):

        prompt = PromptBuilder.build(context)

        response = self.model.generate_content(prompt)

        text = response.text.strip()

        text = text.replace("```json", "")
        text = text.replace("```", "")

        return json.loads(text)
    
    def ask_text(self, prompt: str):

        response = self.model.generate_content(prompt)

        return response.text