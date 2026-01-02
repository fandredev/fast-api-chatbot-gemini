from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """
    Renderiza a página inicial.
    """
    return templates.TemplateResponse(name="index.html", request=request)
