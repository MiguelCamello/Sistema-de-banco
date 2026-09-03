from .conexão import conectar

def criar_tabela_pessoas():
    with conectar() as conexao:
        conexao.execute("""
            CREATE TABLE IF NOT EXISTS pessoas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                cpf TEXT UNIQUE NOT NULL,
                idade INTEGER NOT NULL,
                genero TEXT
            );
            """)

def salvar_pessoa(pessoa):
    with conectar() as conexao:
        cursor=conexao.execute("""
            INSERT INTO pessoas 
            (nome, cpf, idade, genero)
            VALUES (?, ?, ?, ?)
            """, (
                pessoa.nome,
                pessoa.cpf,
                pessoa.idade,
                pessoa.genero
            ))
        return cursor.lastrowid

def deletar_pessoa(pessoaCPF):
    with conectar() as conexao:
        conexao.execute("DELETE FROM pessoas WHERE cpf = ?", (pessoaCPF,))


def buscar_pessoa(pessoaCPF):
    with conectar() as conexao:
        p_busca = conexao.execute("SELECT * FROM pessoas WHERE cpf = ?", (pessoaCPF,)).fetchone()
    p_id, nome, cpf, idade, genero = p_busca

    print(f"""
================================
|   DADOS DA PESSOA   ID: {p_id:<5}|
================================
|                              |
|   Nome: {nome:<21}|  
|   Idade: {str(idade) + " anos":<20}|
|   Genero: {genero:<19}|
|   CPF: {cpf:<22}|
|                              |
================================
""")

def listar_pessoas():
    with conectar() as conexao:
        p_lista = conexao.execute("SELECT * FROM pessoas").fetchall()

        for pessoa in p_lista:
            p_id, nome, cpf, idade, genero = pessoa
            print(f"""
================================
|   DADOS DA PESSOA   ID: {p_id:<5}|
================================
|                              |
|   Nome: {nome:<21}|  
|   Idade: {str(idade) + " anos":<20}|
|   Genero: {genero:<19}|
|   CPF: {cpf:<22}|
|                              |
================================
""")