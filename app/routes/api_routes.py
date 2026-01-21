from fastapi import APIRouter, Request
from slowapi import Limiter
from slowapi.util import get_remote_address

from app.controllers.anime_controller import AnimeController
from app.controllers.health_check_controller import HealthCheckController
from app.models.user_models import UserMessage

anime_controller = AnimeController()
health_controller = HealthCheckController()

router = APIRouter()
limiter = Limiter(key_func=get_remote_address)


@router.get("/health")
def health_check():
    """
    Verifica se o Gemini está funcionando corretamente.
    """
    is_healthy = health_controller.check_gemini_health()
    return {"status": "ok" if is_healthy else "quota_exceeded"}


@router.post("/chat")
@limiter.limit("2/minute")
def chat(request: Request, user_msg: UserMessage):
    """
    Processa uma mensagem do usuário e retorna uma resposta do chatbot.
    """
    result = anime_controller.get_response(user_msg.message)
    return result
