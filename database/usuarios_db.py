from .conexão import conectar

def criar_tabela_usuarios():
    with conectar() as conexao:
        conexao.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                pessoa_id INTEGER NOT NULL,
                banco_id INTEGER NOT NULL,
                telefone TEXT,
                email TEXT NOT NULL,
                senha_hash TEXT NOT NULL,
                saldo INTEGER,
                divida INTEGER,

                FOREIGN KEY (pessoa_id) REFERENCES pessoas(id)
                    ON DELETE CASCADE,
                FOREIGN KEY (banco_id) REFERENCES bancos(id)
                    ON DELETE CASCADE

            )
            """)

def salvar_usuario(usuario):
    with conectar() as conexao:
        conexao.execute("""
            INSERT INTO usuarios
            (pessoa_id, banco_id, telefone, email, senha_hash, saldo, divida)
            VALUES (?, ?, ?, ?, ?, ?, ?)""", (
                usuario.pessoa_id,
                usuario.banco_id,
                usuario.telefone,
                usuario.email,
                usuario.senha_hash,
                usuario.saldo,
                usuario.divida
            ))

def deletar_usuario(usuarioID): # vai apagar todos os usuarios dependentes da pessoa, cuidado!
    with conectar() as conexao:
        conexao.execute("DELETE FROM usuarios WHERE id = ?", (usuarioID,))
        
def buscar_usuario(usuarioID):
    with conectar() as conexao:
        u_busca = conexao.execute("""
            SELECT u.id, u.telefone, u.email, u.senha_hash, u.saldo, u.divida, p.nome, p.cpf, p.idade, p.genero
            FROM usuarios AS u
            JOIN pessoas AS p
                ON u.pessoa_id = p.id
            WHERE u.id = ?
            """, (usuarioID,)).fetchone()
    u_id, telefone, email, senha_hash, saldo, divida, nome, cpf, idade, genero = u_busca
    
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
        
def listar_usuarios(pessoaID=None, bancoID=None): # pode pesquisar os usuarios ligados a uma pessoa ou banco
    query = """
        SELECT u.id, u.telefone, u.email, u.senha_hash, u.saldo, u.divida, p.nome AS pessoa_nome, p.cpf, p.idade, p.genero, b.nome AS banco_nome
        FROM usuarios as u
        JOIN pessoas as p
            ON u.pessoa_id = p.id
        JOIN bancos as b
            ON u.banco_id = b.id
        """
    parametros=[]
    filtros=[]

    if pessoaID is not None:
        parametros.append(pessoaID)
        filtros.append("u.pessoa_id = ?")
    if bancoID is not None:
        parametros.append(bancoID)
        filtros.append("u.banco_id = ?")

    if filtros:
        query += " WHERE " + " AND ".join(filtros)

    with conectar() as conexao:
        u_lista = conexao.execute(query, parametros).fetchall()
    
    for user in u_lista:
        u_id, telefone, email, senha_hash, saldo, divida, nome, cpf, idade, genero, b_nome = user

        print(f"""
================================
|   DADOS DO USUARIO  ID: {u_id:<5}|
================================
|                              |
|   BANCO: {b_nome:<20}|
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