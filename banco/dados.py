from pathlib import Path
import sqlite3

BASE_DIR = Path(__file__).parent.parent
PASTA_DATABASE = BASE_DIR / "database"
PASTA_DATABASE.mkdir(parents=True, exist_ok=True)
BANCO = PASTA_DATABASE / "banco.db"

# Pessoas
def criar_tabela_pessoa():
    with sqlite3.connect(BANCO) as conexao:
        conexao.execute("""
        CREATE TABLE IF NOT EXISTS pessoas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cpf TEXT UNIQUE NOT NULL,
            idade INTEGER NOT NULL,
            genero TEXT,
            telefone TEXT
        )
        """)

def salvar_pessoa(pessoa):
    with sqlite3.connect(BANCO) as conexao:
        conexao.execute("""
        INSERT INTO pessoas 
        (nome, cpf, idade, genero, telefone)
        VALUES (?, ?, ?, ?, ?)
        """, (
            pessoa.nome,
            pessoa.cpf,
            pessoa.idade,
            pessoa.genero,
            pessoa.telefone
        ))

def deletar_pessoa(pessoaCpf):
    with sqlite3.connect(BANCO) as conexao:
        conexao.execute("""
        DELETE FROM pessoas WHERE cpf = ?
        """, (pessoaCpf,))

def listar_pessoas():
    with sqlite3.connect(BANCO) as conexao:
        lista = conexao.execute("""
        SELECT * FROM pessoas
        """).fetchall()
        
        for pessoa in lista:
            id, nome, cpf, idade, genero, telefone = pessoa
            print(f"""
================================
|   DADOS PESSOAIS  ID: {id:<7}|
================================
|                              |
|   Nome: {nome:<21}|  
|   Idade: {str(idade) + " anos":<20}|
|   Genero: {genero:<19}|
|   Telefone: {telefone:<17}|
|   CPF: {cpf:<22}|
|                              |
================================
""")

def buscar_pessoa(pessoaCPF):
    with sqlite3.connect(BANCO) as conexao:
        busca = conexao.execute("""
        SELECT * FROM pessoas WHERE cpf = ?
        """, (pessoaCPF,)).fetchone()
    id, nome, cpf, idade, genero, telefone = busca
    print(f"""
================================
|   DADOS PESSOAIS  ID: {id:<7}|
================================
|                              |
|   Nome: {nome:<21}|  
|   Idade: {str(idade) + " anos":<20}|
|   Genero: {genero:<19}|
|   Telefone: {telefone:<17}|
|   CPF: {cpf:<22}|
|                              |
================================
""")
    
# User

def criar_tabela_usuario():
    with sqlite3.connect(BANCO) as conexao:
        conexao.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cpf TEXT UNIQUE NOT NULL,
            idade INTEGER NOT NULL,
            genero TEXT,
            telefone TEXT,
            email TEXT NOT NULL,
            senha TEXT NOT NULL,
            saldo INTEGER,
            divida INTEGER
        )
        """)

def salvar_usuario(usuario):
    with sqlite3.connect(BANCO) as conexao:
        conexao.execute("""
            INSERT INTO usuarios
            (nome, cpf, idade, genero, telefone, email, senha, saldo, divida)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""", (
                usuario.pessoa.nome,
                usuario.pessoa.cpf,
                usuario.pessoa.idade,
                usuario.pessoa.genero,
                usuario.pessoa.telefone,
                usuario.email,
                usuario.senha,
                usuario.saldo,
                usuario.divida
            ))