import unittest
from http import HTTPStatus
from unittest.mock import patch

import pytest
from fastapi.testclient import TestClient

from main import app


@pytest.mark.route
class TestViewRoutes(unittest.TestCase):
    def setUp(self):
        """Set up the test client for each test case."""
        self.client = TestClient(app)

    def test_should_return_200_when_template_is_rendered(self):
        """Test if the home page renders correctly."""
        response = self.client.get("/")
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertIn("AnimeChat", response.text)

    def test_should_return_200_when_docs_is_called(self):
        """Test if the API documentation is accessible."""
        response = self.client.get("/docs")
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertIn("Anime Chatbot", response.text)


@pytest.mark.route
class TestHealthApi(unittest.TestCase):
    def setUp(self):
        """Set up the test client for each test case."""
        self.client = TestClient(app)

    @patch("app.routes.api_routes.health_controller.check_gemini_health")
    def test_should_return_ok_and_200_when_gemini_is_healthy(self, mock_health):
        """Test if the health route returns 'ok' when Gemini is healthy."""
        mock_health.return_value = True
        response = self.client.get("/api/health")

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.json(), {"status": "ok"})

    @patch("app.routes.api_routes.health_controller.check_gemini_health")
    def test_should_return_quota_exceeded_and_200_when_gemini_fails(self, mock_health):
        """Test if the health route returns 'quota_exceeded' when health check fails."""
        mock_health.return_value = False
        response = self.client.get("/api/health")

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.json(), {"status": "quota_exceeded"})
