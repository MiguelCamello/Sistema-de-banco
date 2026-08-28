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
            pessoa_id INTEGER PRIMARY KEY AUTOINCREMENT,
            pessoa_nome TEXT NOT NULL,
            pessoa_cpf TEXT UNIQUE NOT NULL,
            pessoa_idade INTEGER NOT NULL,
            pessoa_genero TEXT,
            pessoa_telefone TEXT
        )
        """)

def salvar_pessoa(pessoa):
    with sqlite3.connect(BANCO) as conexao:
        conexao.execute("""
        INSERT INTO pessoas 
        (pessoa_nome, pessoa_cpf, pessoa_idade, pessoa_genero, pessoa_telefone)
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
        DELETE FROM pessoas WHERE pessoa_cpf = ?
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
        pessoa_busca = conexao.execute("""
        SELECT * FROM pessoas WHERE pessoa_cpf = ?
        """, (pessoaCPF,)).fetchone()
    id, nome, cpf, idade, genero, telefone = pessoa_busca
    print(f"""
================================
|   DADOS PESSOA   ID: {id:<8}|
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
    
# Usuario

def criar_tabela_usuario():
    with sqlite3.connect(BANCO) as conexao:
        conexao.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            usuario_id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario_nome TEXT NOT NULL,
            usuario_cpf TEXT UNIQUE NOT NULL,
            usuario_idade INTEGER NOT NULL,
            usuario_genero TEXT,
            usuario_telefone TEXT,
            usuario_email TEXT NOT NULL,
            usuario_senha TEXT NOT NULL,
            usuario_saldo INTEGER,
            usuario_divida INTEGER
        )
        """)

def salvar_usuario(usuario):
    with sqlite3.connect(BANCO) as conexao:
        conexao.execute("""
            INSERT INTO usuarios
            (usuario_nome, usuario_cpf, usuario_idade, usuario_genero, usuario_telefone, usuario_email, usuario_senha, usuario_saldo, usuario_divida)
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
        
def buscar_usuario(usuarioCpf):
    with sqlite3.connect(BANCO) as conexao:
        usuario_busca = conexao.execute("""
        SELECT * FROM usuarios WHERE usuario_cpf = ?
        """, (usuarioCpf,)).fetchone()
    id, nome, cpf, idade, genero, telefone, email, senha, saldo, divida = usuario_busca
    print(f"""
================================
|   DADOS USUARIO  ID: {id:<8}|
================================
|                              |
|   Nome: {nome:<21}|  
|   Idade: {str(idade) + " anos":<20}|
|   Genero: {genero:<19}|
|   Telefone: {telefone:<17}|
|   CPF: {cpf:<22}|
|   Email: {email:<20}|
|   Senha: {senha:<20}|
|   saldo: {saldo:<20}|
|   Divida: {divida:<19}|
|                              |
================================
""")
        
# def listar_usuario():
#     with sqlite3.connect(BANCO) as conexao:
#         usuario_lista = conexao.execute("""]
#             SELECT * FROM usuarios
#             """).fetchall()
#     for user in 
#     #terminar dps