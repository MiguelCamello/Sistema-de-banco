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
                pessoa_genero TEXT
            )
            """)

def salvar_pessoa(pessoa):
    with sqlite3.connect(BANCO) as conexao:
        cursor = conexao.execute("""
            INSERT INTO pessoas 
            (pessoa_nome, pessoa_cpf, pessoa_idade, pessoa_genero)
            VALUES (?, ?, ?, ?)
            """, (
                pessoa.nome,
                pessoa.cpf,
                pessoa.idade,
                pessoa.genero
            ))
        pessoa.pessoa_id = cursor.lastrowid


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
            id, nome, cpf, idade, genero = pessoa
            print(f"""
================================
|   DADOS DA PESSOA   ID: {id:<5}|
================================
|                              |
|   Nome: {nome:<21}|  
|   Idade: {str(idade) + " anos":<20}|
|   Genero: {genero:<19}|
|   CPF: {cpf:<22}|
|                              |
================================
""")

def buscar_pessoa(pessoaCPF):
    with sqlite3.connect(BANCO) as conexao:
        pessoa_busca = conexao.execute("""
            SELECT * FROM pessoas WHERE pessoa_cpf = ?
            """, (pessoaCPF,)).fetchone()
    pessoa_id, nome, cpf, idade, genero = pessoa_busca
    print(f"""
================================
|   DADOS DA PESSOA   ID: {pessoa_id:<5}|
================================
|                              |
|   Nome: {nome:<21}|  
|   Idade: {str(idade) + " anos":<20}|
|   Genero: {genero:<19}|
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
                pessoa_id INTEGER NOT NULL,
                usuario_telefone TEXT,
                usuario_email TEXT NOT NULL,
                usuario_senha TEXT NOT NULL,
                usuario_saldo INTEGER,
                usuario_divida INTEGER,

                FOREIGN KEY (pessoa_id) REFERENCES pessoas(pessoa_id)
        )
        """)

def salvar_usuario(usuario):
    with sqlite3.connect(BANCO) as conexao:
        conexao.execute("""
            INSERT INTO usuarios
            (pessoa_id, usuario_telefone, usuario_email, usuario_senha, usuario_saldo, usuario_divida)
            VALUES (?, ?, ?, ?, ?, ?)""", (
                usuario.pessoa.pessoa_id,
                usuario.telefone,
                usuario.email,
                usuario.senha,
                usuario.saldo,
                usuario.divida
        ))
        
def buscar_usuario(usuarioID):    # Pode ser otimizado mais tarde usando JOIN, só falta aprender usar!!!!!!
    with sqlite3.connect(BANCO) as conexao:
        usuario_busca = conexao.execute("""
            SELECT * FROM usuarios WHERE usuario_id = ?
            """, (usuarioID,)).fetchone()
        usuario_id, pessoa_id, telefone, email, senha, saldo, divida = usuario_busca

        pessoa_busca = conexao.execute("""
            SELECT pessoa_nome, pessoa_cpf, pessoa_idade, pessoa_genero FROM pessoas WHERE pessoa_id = ?   
            """, (pessoa_id,)).fetchone()
        nome, cpf, idade, genero = pessoa_busca

    print(f"""
================================
|   DADOS DO USUARIO  ID: {usuario_id:<5}|
================================
|                              |
|   Nome: {nome:<21}|  
|   Idade: {str(idade) + " anos":<20}|
|   Genero: {genero:<19}|
|   CPF: {cpf:<22}|
|   Telefone: {telefone:<17}|
|   Email: {email:<20}|
|   Senha: {senha:<20}|
|   saldo: {saldo:<20}|
|   Divida: {divida:<19}|
|                              |
================================
""")
        
def listar_usuario():
    with sqlite3.connect(BANCO) as conexao:
        usuario_lista = conexao.execute("""
            SELECT * FROM usuarios
            """).fetchall()
        
    for user in usuario_lista:
        usuario_id, pessoa_id, telefone, email, senha, saldo, divida = user

        pessoa_busca = conexao.execute("""
            SELECT pessoa_nome, pessoa_cpf, pessoa_idade, pessoa_genero FROM pessoas WHERE pessoa_id = ?
            """, (pessoa_id,)).fetchone()
        nome, cpf, idade, genero = pessoa_busca
        print(f"""
================================
|   DADOS DO USUARIO  ID: {usuario_id:<5}|
================================
|                              |
|   Nome: {nome:<21}|  
|   Idade: {str(idade) + " anos":<20}|
|   Genero: {genero:<19}|
|   CPF: {cpf:<22}|
|   Telefone: {telefone:<17}|
|   Email: {email:<20}|
|   Senha: {senha:<20}|
|   saldo: {saldo:<20}|
|   Divida: {divida:<19}|
|                              |
================================
""")