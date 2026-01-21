import os

from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI  # noqa: E402
from fastapi.staticfiles import StaticFiles  # noqa: E402
from slowapi import _rate_limit_exceeded_handler  # noqa: E402
from slowapi.errors import RateLimitExceeded  # noqa: E402
from slowapi.middleware import SlowAPIMiddleware  # noqa: E402
from starlette.requests import Request  # noqa: E402
from starlette.responses import Response  # noqa: E402

from app.routes import api_routes, view_routes  # noqa: E402
from app.utils.logger import logger  # noqa: E402

logger.info("Variáveis de ambiente carregadas com sucesso")
logger.info(f"Servidor iniciado com modelo: {os.getenv('GEMINI_MODEL_NAME')}")

app = FastAPI(
    title="Anime Chatbot",
    summary="Anime Chatbot é um chatbot que responde perguntas sobre anime.",
    version="1.0",
    contact={
        "name": "Felipe André",
        "url": "https://developer-felipe-andre.vercel.app/",
        "email": "profissionalf.andre@gmail.com",
    },
)
app.state.limiter = api_routes.limiter


@app.exception_handler(RateLimitExceeded)
def _rate_limit_exceeded_handler_wrapper(request: Request, exc: Exception) -> Response:
    return _rate_limit_exceeded_handler(request, exc)  # type: ignore


app.add_middleware(SlowAPIMiddleware)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(view_routes.router)
app.include_router(api_routes.router, prefix="/api")

if __name__ == "__main__":
    import uvicorn

    port = int(os.getenv("APP_PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
