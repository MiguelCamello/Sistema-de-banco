from .conexão import conectar

def criar_tabela_bancos():
    with conectar() as conexao:
        conexao.execute("""
            CREATE TABLE IF NOT EXISTS bancos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL
            )
            """) 

def salvar_banco(banco):
    with conectar() as conexao:
        cursor = conexao.execute("""
            INSERT INTO bancos (nome)
            VALUES (?)
            """, (banco.nome,))

        return cursor.lastrowid