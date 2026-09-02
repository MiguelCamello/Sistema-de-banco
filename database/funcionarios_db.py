from .conexão import conectar

def criar_tabela_funcionarios():
    with conectar() as conexao:
        conexao.execute("""
            CREATE TABLE IF NOT EXISTS funcionarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                pessoa_id INTEGER NOT NULL,
                banco_id INTEGER NOT NULL,
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
            (pessoa_id, banco_id, emailStaff, senhaStaff_hash, salario)
            VALUES (?, ?, ?, ?, ?)
            """, (
                funcionario.pessoa_id,
                funcionario.banco_id,
                funcionario.emailStaff,
                funcionario.senhaStaff_hash,
                funcionario.salario
            ))