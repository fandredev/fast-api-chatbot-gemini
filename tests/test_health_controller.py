import unittest
from unittest.mock import MagicMock, patch

import pytest

from app.controllers.health_check_controller import HealthCheckController


@pytest.mark.unit
class TestHealthCheckController(unittest.TestCase):
    def setUp(self):
        """Set up the controller for each test case."""
        self.controller = HealthCheckController()

    def test_should_return_true_when_client_responds_successfully(self):
        """Test if it returns True when the client responds successfully."""
        self.controller.client = MagicMock()
        self.controller.client.models.generate_content.return_value = MagicMock()

        self.assertTrue(self.controller.check_gemini_health())

    def test_should_return_false_when_no_client_is_initialized(self):
        """Test if it returns False when no client is initialized."""
        self.controller.client = None

        self.assertFalse(self.controller.check_gemini_health())

    def test_should_return_false_when_api_raises_exception(self):
        """Explicitly test the 'except Exception' block of the controller."""
        self.controller.client = MagicMock()

        # Simulate an API failure (e.g., timeout, network error, quota limit)
        self.controller.client.models.generate_content.side_effect = Exception(
            "API Error"
        )

        with patch("app.controllers.health_check_controller.logger") as mock_logger:
            result = self.controller.check_gemini_health()

            self.assertFalse(result)
            mock_logger.warning.assert_called_once_with(
                "Falha no Health Check do Gemini: API Error"
            )
