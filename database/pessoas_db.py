from .conexão import conectar

def criar_tabela_pessoa():
    with conectar() as conexao:
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
    with conectar() as conexao:
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
    with conectar() as conexao:
        conexao.execute("""
            DELETE FROM pessoas WHERE pessoa_cpf = ?
            """, (pessoaCpf,))

def listar_pessoas():
    with conectar() as conexao:
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
    with conectar() as conexao:
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