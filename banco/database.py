import sqlite3

def criar_tabela_pessoa():
    with sqlite3.connect("database/banco.db") as conexao:
        conexao.execute("""
CREATE TABLE IF NOT EXISTS pessoas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cpf TEXT UNIQUE NOT NULL,
    idade INTEGER,
    genero TEXT,
    telefone TEXT
)
""")


def salvar_pessoa(pessoa):
    with sqlite3.connect("database/banco.db") as conexao:
        conexao.execute("""
INSERT INTO pessoas (nome, cpf, idade, genero, telefone)
VALUES (?, ?, ?, ?, ?)
""", (
    pessoa.nome,
    pessoa.cpf,
    pessoa.idade,
    pessoa.genero,
    pessoa.telefone
))

def buscar_pessoa(pessoa):
    with sqlite3.connect("database/banco.db") as conexao:
        conexao.execute("""
SELECT * FROM pessoas WHERE cpf = ?
""", (pessoa.cpf,))