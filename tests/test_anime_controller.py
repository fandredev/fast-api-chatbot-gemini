import unittest
from unittest.mock import MagicMock, patch

import pytest

from app.controllers.anime_controller import AnimeController


@pytest.mark.unit
class TestAnimeController(unittest.TestCase):
    @patch("app.controllers.anime_controller.genai.Client")
    @patch("app.controllers.anime_controller.os.getenv")
    def setUp(self, mock_getenv, mock_client_class):
        """Set up the controller with mocked environment and client."""
        mock_getenv.side_effect = lambda key: {
            "GEMINI_API_KEY": "fake_key",
            "GEMINI_MODEL_NAME": "fake_model",
        }.get(key)

        self.mock_client = MagicMock()
        mock_client_class.return_value = self.mock_client

        self.controller = AnimeController()

    def test_should_yield_text_when_api_responds_successfully(self):
        """Test if get_streaming_response yields correct text."""
        mock_chunk = MagicMock()
        mock_chunk.text = "Naruto is a ninja."
        self.controller.chat_session.send_message_stream.return_value = [mock_chunk]

        result = list(self.controller.get_streaming_response("Who is Naruto?"))

        self.assertEqual(result, ["Naruto is a ninja."])

    def test_should_yield_error_when_api_key_is_missing(self):
        """Test if get_streaming_response yields error when API key is missing."""
        self.controller.api_key = None

        result = list(self.controller.get_streaming_response("Hello"))

        self.assertEqual(
            result, ["Erro: Chave de API inválida ou sessão não inicializada."]
        )

    def test_should_yield_technical_error_when_api_raises_generic_exception(self):
        """Test if get_streaming_response handles generic exceptions gracefully."""
        self.controller.chat_session.send_message_stream.side_effect = Exception(
            "Generic Error"
        )

        with patch("app.controllers.anime_controller.logger") as mock_logger:
            result = list(self.controller.get_streaming_response("Hello"))

            self.assertEqual(
                result, ["Erro: Ops! Tive um problema técnico no streaming."]
            )
            mock_logger.error.assert_called()

    def test_should_yield_quota_error_when_api_raises_429_exception(self):
        """Test if get_streaming_response handles 429 quota errors specifically."""
        self.controller.chat_session.send_message_stream.side_effect = Exception(
            "error 429: Quota exceeded"
        )

        result = list(self.controller.get_streaming_response("Hello"))

        self.assertIn("Limite de cota excedido", result[0])
        self.assertIn("Erro:", result[0])

    def test_should_initialize_chat_session_when_client_is_valid(self):
        """Test if _init_chat_session correctly sets up the chat session."""
        self.assertIsNotNone(self.controller.chat_session)
        self.mock_client.chats.create.assert_called_once()
