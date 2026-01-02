from fastapi import APIRouter
from pydantic import BaseModel
from app.controllers.anime_controller import AnimeController

router = APIRouter()
anime_controller = AnimeController()


class UserMessage(BaseModel):
    message: str


@router.get("/health")
def health_check():
    is_healthy = anime_controller.check_health()
    return {"status": "ok" if is_healthy else "quota_exceeded"}


@router.post("/chat")
def chat(user_msg: UserMessage):
    result = anime_controller.get_response(user_msg.message)
    return result
