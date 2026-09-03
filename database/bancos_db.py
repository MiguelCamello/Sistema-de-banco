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

def deletar_banco(bancoID):
    with conectar() as conexao:
        conexao.execute("DELETE FROM bancos WHERE id = ?", (bancoID,))

def buscar_banco(bancoID):
    with conectar() as conexao:
        b_busca = conexao.execute("SELECT * FROM bancos WHERE id = ?", (bancoID,)).fetchone()
    b_id, nome = b_busca

    print(f"""
================================
|   DADOS DO BANCO  ID: {b_id:<7}|
================================
|                              |
|   Nome: {nome:<21}|  
|                              |
================================
""")


def listar_bancos():
    with conectar() as conexao:
        b_lista = conexao.execute("SELECT * FROM bancos").fetchall()

    for banco in b_lista:
        b_id, nome = banco
        
        print(f"""
================================
|   DADOS DO BANCO  ID: {b_id:<7}|
================================
|                              |
|   Nome: {nome:<21}|  
|                              |
================================
""")