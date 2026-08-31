from .conexão import conectar

def criar_tabela_usuario():
    with conectar() as conexao:
        conexao.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                usuario_id INTEGER PRIMARY KEY AUTOINCREMENT,
                pessoa_id INTEGER NOT NULL,
                usuario_telefone TEXT,
                usuario_email TEXT NOT NULL,
                usuario_senha TEXT NOT NULL,
                usuario_senha_hash TEXT NOT NULL,
                usuario_saldo INTEGER,
                usuario_divida INTEGER,

                FOREIGN KEY (pessoa_id) REFERENCES pessoas(pessoa_id)
        )
        """)

def salvar_usuario(usuario):
    with conectar() as conexao:
        conexao.execute("""
            INSERT INTO usuarios
            (pessoa_id, usuario_telefone, usuario_email, usuario_senha, usuario_senha_hash, usuario_saldo, usuario_divida)
            VALUES (?, ?, ?, ?, ?, ?, ?)""", (
                usuario.pessoa_id,
                usuario.telefone,
                usuario.email,
                usuario.senha,
                usuario.senha_hash,
                usuario.saldo,
                usuario.divida
        ))
        
def buscar_usuario(usuarioID):    # Pode ser otimizado mais tarde usando JOIN, só falta aprender usar!!!!!!
    with conectar() as conexao:
        usuario_busca = conexao.execute("""
            SELECT
            usuario_id, pessoa_id, usuario_telefone, usuario_email, usuario_senha_hash, usuario_saldo, usuario_divida
            FROM usuarios WHERE usuario_id = ?
            """, (usuarioID,)).fetchone()
        usuario_id, pessoa_id, telefone, email, senha_hash, saldo, divida = usuario_busca

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
            SELECT
            usuario_id, pessoa_id, usuario_telefone, usuario_email, usuario_senha_hash, usuario_saldo, usuario_divida
            FROM usuarios
            """).fetchall()
        
    for user in usuario_lista:
        usuario_id, pessoa_id, telefone, email, senha_hash, saldo, divida = user

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
|   Senha_Hash:                |
|   {senha_hash:<27}|
|   saldo: {saldo:<20}|
|   Divida: {divida:<19}|
|                              |
================================
""")