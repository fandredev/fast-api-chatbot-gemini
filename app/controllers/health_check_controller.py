import os
from google import genai
from google.genai import types
from app.utils.logger import logger


class HealthCheckController:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        self.model = os.getenv("GEMINI_MODEL_NAME")
        self.client = None

        if self.api_key:
            self.client = genai.Client(api_key=self.api_key)
        else:
            logger.warning("GEMINI_API_KEY não encontrada no HealthCheckController")

    def check_gemini_health(self) -> bool:
        """Verifica se a chave da API do Gemini tem cota disponível."""
        if not self.client:
            return False
        try:
            self.client.models.generate_content(
                model=self.model,
                contents="ping",
                config=types.GenerateContentConfig(max_output_tokens=1),
            )
            return True
        except Exception as e:
            logger.warning(f"Falha no Health Check do Gemini: {e}")
            return False
