import os
from google import genai
from google.genai import types
from app.utils.logger import logger


class AnimeController:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        self.model = os.getenv("GEMINI_MODEL_NAME")
        self.client = None
        self.chat_session = None

        if self.api_key:
            self.client = genai.Client(api_key=self.api_key)
            self._init_chat_session()
        else:
            logger.warning("GEMINI_API_KEY não encontrada nas variáveis de ambiente")

    def _init_chat_session(self):
        """Initialize the chat session with system instruction and configuration."""
        system_instruction = """

            ## PERSONA:
            Você é o AnimeChat, um assistente especialista em animes, mangás e cultura pop japonesa.
            Responda sempre em Português (PT-BR). Sua personalidade é amigável.
            REGRA DE OURO: Suas respostas devem ser CURTAS e OBJETIVAS (máximo 2 parágrafos pequenos).
            Fale apenas sobre animes/mangas. Se perguntarem fora do tema, recuse educadamente.

            ## FORMATAÇÃO DE SAÍDA:
            
            #### Exemplo 1:

            Se a pessoa perguntar: "Quem é Naruto Uzumaki?",
            Você deve responder: "Naruto Uzumaki é um personagem do anime e mangá Naruto..."

            #### Exemplo 2:

            Se a pessoa perguntar: "Qual é o atual presidente do Japão?",
            Você deve responder: "Não posso responder isso, pois apenas respondo sobre animes, mangás e cultura pop japonesa."
            
        """

        if self.client:
            try:
                self.chat_session = self.client.chats.create(
                    model=self.model,
                    config=types.GenerateContentConfig(
                        system_instruction=system_instruction,
                        temperature=0.4,
                        max_output_tokens=200,
                    ),
                )
            except Exception as e:
                logger.error(f"Erro ao criar sessão de chat: {e}", exc_info=True)
                self.chat_session = None

    def get_response(self, message: str) -> dict:
        """Return a dictionary with Gemini's response about anime/manga using the chat method."""
        if not self.api_key or not self.client or not self.chat_session:
            return {
                "error": "Chave de API inválida ou sessão não inicializada.",
                "text": "Desculpe, a chave da API não foi configurada corretamente.",
            }
        try:
            response = self.chat_session.send_message(message)
            return {"text": response.text}

        except Exception as e:
            logger.error(
                f"Erro ao processar mensagem - {type(e).__name__}: {str(e)}",
                exc_info=True,
            )

            error_msg = "Ops! Tive um problema técnico agora."
            if "429" in str(e):
                error_msg = "Limite de cota excedido (Quota 429). Tente novamente em alguns minutos."
                logger.warning("Limite de cota da API Gemini atingido (429)")

            return {"error": error_msg, "text": error_msg}
