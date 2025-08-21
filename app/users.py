import json
from pathlib import Path

USERS_FILE = Path("app/users.json")

def load_users():
    if USERS_FILE.exists():
        with open(USERS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_users(users):
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, indent=2)

def get_user(username: str):
    users = load_users()
    return users.get(username)

def save_user(user):
    # Salva as alterações no banco de dados
    with open("app/users.json", "r+", encoding="utf-8") as f:
        users = json.load(f)
        users[user["username"]] = user
        f.seek(0)
        json.dump(users, f, indent=4, ensure_ascii=False)
        f.truncate()
    
def get_all_users():
    # Retorna todos os usuários do banco de dados
    with open("app/users.json", "r", encoding="utf-8") as f:
        return json.load(f).values()

