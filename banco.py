import sqlite3

def conectar():
    return sqlite3.connect("usuarios.db")


def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()


def inserir_usuario(nome, email):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO usuarios (nome, email) VALUES (?, ?)",
        (nome, email)
    )

    conn.commit()
    conn.close()


def listar_usuarios():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usuarios")

    usuarios = cursor.fetchall()

    conn.close()

    return usuarios
def atualizar_usuario(id, nome, email):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE usuarios SET nome = ?, email = ? WHERE id = ?",
        (nome, email, id)
    )

    conn.commit()
    conn.close()


def deletar_usuario(id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM usuarios WHERE id = ?",
        (id,)
    )

    conn.commit()
    conn.close()
