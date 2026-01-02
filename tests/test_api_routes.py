from main import app
from fastapi.testclient import TestClient
from http import HTTPStatus

client = TestClient(app)


def test_should_return_200_when_template_is_rendered():
    response = client.get("/")
    assert response.status_code == HTTPStatus.OK
    assert "AnimeChat" in response.text


def test_should_return_200_when_docs_is_called():
    response = client.get("/docs")
    assert response.status_code == HTTPStatus.OK
    assert "Anime Chatbot" in response.text
