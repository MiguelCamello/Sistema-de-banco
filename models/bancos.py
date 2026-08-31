class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []
        self.usuarios = []

    def cadastrar_usuario(self, usuario):
        if usuario in self.usuarios:
            raise ValueError("Esse usuario já está cadastrado")
        self.usuarios.append(usuario)

    def remover_usuario(self, usuario):
        self.usuarios.remove(usuario)

    def contratar_funcionario(self, funcionario):
        if funcionario in self.funcionarios:
            raise ValueError("Esse funcionario já está contratado")
        self.funcionarios.append(funcionario)

    def demitir_funcionario(self, funcionario):
        self.funcionarios.remove(funcionario)

    def lista_users(self):
        print(f"""
================================
|        {self.nome:<22}|
================================
|                              |
|   Usuarios:                  |
|                              |
{"\n".join(f"|   {u.pessoa.nome:<27}|" for u in self.usuarios)}
|                              |
================================
""")

    def lista_staff(self):
        print(f"""
================================
|        {self.nome:<22}|
================================
|                              |
|   Funcionarios:              |
|                              |
{"\n".join(f"|   {u.pessoa.nome:<27}|" for u in self.funcionarios)}
|                              |
================================
        """)

