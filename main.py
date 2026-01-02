from dotenv import load_dotenv
import os

# Carrega variáveis de ambiente ANTES de importar outros módulos
load_dotenv()

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes import view_routes, api_routes
from app.utils.logger import logger

logger.info("Variáveis de ambiente carregadas com sucesso")
logger.info(f"Servidor iniciado com modelo: {os.getenv('GEMINI_MODEL_NAME')}")

app = FastAPI(title="Anime Chatbot")

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(view_routes.router)
app.include_router(api_routes.router, prefix="/api")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
