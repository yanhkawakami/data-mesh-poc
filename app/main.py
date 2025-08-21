from fastapi import FastAPI, Form, Request, UploadFile, File
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path
import csv
import os

from app.users import get_user, save_user, get_all_users

app = FastAPI()
BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))
DATA_DIR = Path(__file__).resolve().parent.parent / "data"
DATA_DIR.mkdir(exist_ok=True)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login")
async def login(username: str = Form(...), password: str = Form(...)):
    user = get_user(username)
    if not user or user["password"] != password:
        return HTMLResponse("Credenciais inválidas", status_code=401)
    return RedirectResponse(f"/dashboard?username={username}", status_code=302)

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request, username: str):
    user = get_user(username)
    all_dominios = [f.stem for f in DATA_DIR.glob("*.csv")]
    todos_usuarios = [u["username"] for u in get_all_users()]  # Função para obter todos os usuários
    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "username": username,
        "user": user,
        "dominios_disponiveis": all_dominios,
        "todos_usuarios": todos_usuarios,
    })

@app.get("/download/{dominio}")
async def download_csv(dominio: str, username: str):
    user = get_user(username)
    if "read" not in user["permissoes"].get(dominio, []):
        return HTMLResponse("Você não tem permissão de leitura para esse domínio.", status_code=403)

    file_path = DATA_DIR / f"{dominio}.csv"
    print(f"File path: {file_path}")  # Debugging line to check the file path
    if not file_path.exists():
        return HTMLResponse("Arquivo não encontrado", status_code=404)

    return RedirectResponse(url=f"/static/{file_path.relative_to(BASE_DIR)}")

@app.post("/upload")
async def upload_csv(
    request: Request,
    file: UploadFile = File(...),
    dominio: str = Form(...),
    usuarios: list[str] = Form(...),
    username: str = Form(...),
):
    user = get_user(username)

    # Verifica se o usuário tem permissão de escrita
    if "write" not in user["permissoes"].get(dominio, []):
        return HTMLResponse("Você não tem permissão de escrita para esse domínio.", status_code=403)

    # Salva o arquivo no diretório de dados
    file_path = DATA_DIR / f"{dominio}.csv"
    with open(file_path, "wb") as f:
        f.write(await file.read())

    # Atualiza as permissões para os usuários selecionados
    for usuario in usuarios:
        target_user = get_user(usuario)
        if dominio not in target_user["permissoes"]:
            target_user["permissoes"][dominio] = []
        if "read" not in target_user["permissoes"][dominio]:
            target_user["permissoes"][dominio].append("read")
        save_user(target_user)  # Função para salvar as alterações no banco de dados

    return RedirectResponse(f"/dashboard?username={username}", status_code=302)