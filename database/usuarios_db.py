from .conexão import conectar

def criar_tabela_usuario():
    with conectar() as conexao:
        conexao.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                pessoa_id INTEGER NOT NULL,
                telefone TEXT,
                email TEXT NOT NULL,
                senha TEXT NOT NULL,
                senha_hash TEXT NOT NULL,
                saldo INTEGER,
                divida INTEGER,

                FOREIGN KEY (pessoa_id) REFERENCES pessoas(id)
                    ON DELETE CASCADE
        )
        """)

def salvar_usuario(obj_usuario):
    with conectar() as conexao:
        conexao.execute("""
            INSERT INTO usuarios
            (pessoa_id, telefone, email, senha, senha_hash, saldo, divida)
            VALUES (?, ?, ?, ?, ?, ?, ?)""", (
                obj_usuario.pessoa_id,
                obj_usuario.telefone,
                obj_usuario.email,
                obj_usuario.senha,
                obj_usuario.senha_hash,
                obj_usuario.saldo,
                obj_usuario.divida
        ))

def deletar_usuario(usuarioID): # vai apagar todos os usuarios dependentes da pessoa
    with conectar() as conexao:
        conexao.execute("""
DELETE FROM usuarios WHERE id = ?
""", (usuarioID,))
        
def buscar_usuario(usuarioID):
    with conectar() as conexao:
        usuario_busca = conexao.execute("""
        SELECT u.id, u.telefone, u.email, u.senha_hash, u.saldo, u.divida, p.nome, p.cpf, p.idade, p.genero
        FROM usuarios AS u
        JOIN pessoas AS p
            ON u.pessoa_id = p.id
        WHERE u.id = ?
        """, (usuarioID,)).fetchone()
    u_id, telefone, email, senha_hash, saldo, divida, nome, cpf, idade, genero = usuario_busca
    
    print(f"""
================================
|   DADOS DO USUARIO  ID: {u_id:<5}|
================================
|                              |
|   Nome: {nome:<21}|  
|   Idade: {str(idade) + " anos":<20}|
|   Genero: {genero:<19}|
|   CPF: {cpf:<22}|
|   Telefone: {telefone:<17}|
|   Email: {email:<20}|
|   Senha_hash:                |
|   {senha_hash:<27}|
|   saldo: {saldo:<20}|
|   Divida: {divida:<19}|
|                              |
================================
""")
        
def listar_usuario(): 
    with conectar() as conexao:
        usuario_lista = conexao.execute("""
                SELECT u.id, u.telefone, u.email, u.senha_hash, u.saldo, u.divida, p.nome, p.cpf, p.idade, p.genero
                FROM usuarios AS u
                JOIN pessoas AS p
                    ON u.pessoa_id = p.id;
            """).fetchall()

    for user in usuario_lista:
        u_id, telefone, email, senha_hash, saldo, divida, nome, cpf, idade, genero = user

        print(f"""
================================
|   DADOS DO USUARIO  ID: {u_id:<5}|
================================
|                              |
|   Nome: {nome:<21}|  
|   Idade: {str(idade) + " anos":<20}|
|   Genero: {genero:<19}|
|   CPF: {cpf:<22}|
|   Telefone: {telefone:<17}|
|   Email: {email:<20}|
|   Senha_Hash:                |
|   {senha_hash:<27}|
|   saldo: {saldo:<20}|
|   Divida: {divida:<19}|
|                              |
================================
""")