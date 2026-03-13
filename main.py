from fastapi import FastAPI

app = FastAPI()

usuarios = []

@app.get("/")
def inicio():
    return {"mensagem": "API funcionando"}

@app.get("/usuarios")
def listar_usuarios():
    return usuarios

@app.post("/usuarios")
def cadastrar_usuario(nome: str, email: str):
    usuario = {"nome": nome, "email": email}
    usuarios.append(usuario)
    return {"mensagem": "Usuário cadastrado", "usuario": usuario}
