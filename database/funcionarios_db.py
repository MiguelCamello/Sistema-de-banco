from .conexão import conectar

def criar_tabela_funcionarios():
    with conectar() as conexao:
        conexao.execute("""
            CREATE TABLE IF NOT EXISTS funcionarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                pessoa_id INTEGER NOT NULL,
                banco_id INTEGER NOT NULL,
                telefone TEXT NOT NULL,
                emailStaff TEXT NOT NULL,
                senhaStaff_hash TEXT NOT NULL,
                salario INTEGER,

                FOREIGN KEY (pessoa_id) REFERENCES pessoas(id)
                    ON DELETE CASCADE,
                FOREIGN KEY (banco_id) REFERENCES bancos(id)
                    ON DELETE CASCADE
            );
            """)

def salvar_funcionario(funcionario):
    with conectar() as conexao:
        conexao.execute("""
            INSERT INTO funcionarios 
            (pessoa_id, banco_id, telefone, emailStaff, senhaStaff_hash, salario)
            VALUES (?, ?, ?, ?, ?, ?)
            """, (
                funcionario.pessoa_id,
                funcionario.banco_id,
                funcionario.telefone,
                funcionario.emailStaff,
                funcionario.senhaStaff_hash,
                funcionario.salario
            ))
        
def deletar_funcionario(funcionarioID):
    with conectar() as conexao:
        conexao.execute("DELETE FROM funcionarios WHERE id = ?", (funcionarioID,))
        
def buscar_funcionario(funcionarioID):
    with conectar() as conexao:
        f_busca = conexao.execute("""
        SELECT f.id, f.telefone, f.emailStaff, f.senhaStaff_hash, f.salario, p.nome AS pessoa_nome, p.cpf, p.idade, p.genero, b.nome AS banco_nome
        FROM funcionarios AS f
        JOIN pessoas AS p
            ON f.pessoa_id = p.id
        JOIN bancos AS b
            ON f.banco_id = b.id
        WHERE funcionario_id = ?
""", (funcionarioID,)).fetchone()
        
        f_id, telefone, emailStaff, senhaStaff_hash, salario, p_nome, cpf, idade, genero, b_nome = f_busca

        print(f"""
================================
|   DADOS DO STAFF  ID: {f_id:<5}|
================================
|                              |
|   BANCO: {b_nome:<20}|
|                              |
|   Nome: {p_nome:<21}|  
|   Idade: {str(idade) + " anos":<20}|
|   Genero: {genero:<19}|
|   CPF: {cpf:<22}|
|   Telefone: {telefone:<17}|
|   Email: {emailStaff:<20}|
|   Senha_Hash:                |
|   {senhaStaff_hash:<27}|
|   saldo: {salario:<20}|
|                              |
================================
""")


def listar_funcionarios(pessoaID=None, bancoID=None):
    query = """
        SELECT f.id, f.telefone, f.emailStaff, f.senhaStaff_hash, f.salario, p.nome, p.cpf, p.idade, p.genero, b.nome
        FROM funcionarios AS f
        JOIN pessoas AS p
            ON f.pessoa_id = p.id
        JOIN bancos AS b
            ON f.banco_id = b.id
        """
    parametros = []
    filtros = []

    if pessoaID is not None:
        parametros.append(pessoaID)
        filtros.append("pessoa_id = ?")

    if bancoID is not None:
        parametros.append(bancoID)
        filtros.append("banco_id = ?")

    if filtros:
        query += " WHERE " + " AND ".join(filtros)

    with conectar() as conexao:
        f_lista = conexao.execute(query, parametros).fetchall()

    for staff in f_lista:
        f_id, telefone, emailStaff, senhaStaff_hash, salario, p_nome, cpf, idade, genero, b_nome = staff

        print(f"""
================================
|   DADOS DO STAFF  ID: {f_id:<5}|
================================
|                              |
|   BANCO: {b_nome:<20}|
|                              |
|   Nome: {p_nome:<21}|  
|   Idade: {str(idade) + " anos":<20}|
|   Genero: {genero:<19}|
|   CPF: {cpf:<22}|
|   Telefone: {telefone:<17}|
|   Email: {emailStaff:<20}|
|   SenhaStaff_Hash:            |
|   {senhaStaff_hash:<27}|
|   salario: {salario:<18}|
|                              |
================================
""")