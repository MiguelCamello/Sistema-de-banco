class Pessoa:
    def __init__(self, nome, cpf, idade, genero):
        self.nome = nome
        self.cpf = str(cpf)
        self.idade = int(idade)
        self.genero = genero
        
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

class Usuario:
    def __init__(self, pessoa, telefone, email, senha):
        self.pessoa = pessoa # usuario.pessoa.nome
        self.telefone = telefone
        self.email = email
        self.senha = senha 
        self.saldo = 0
        self.divida = 0

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("O valor de deposito deve ser positivo")
        self.saldo += valor

    def retirar(self, valor):
        if valor <= 0:
            raise ValueError("O valor de retirada deve ser positivo")
        if valor > self.saldo: # se for retirar mais do que tem, fica individado
            self.divida += valor - self.saldo
            self.saldo = 0
        else:
            self.saldo -= valor

    def emprestimo(self, valor):
        if valor <= 0:
            raise ValueError("O valor de emprestimo deve ser positivo")
        self.saldo += valor
        self.divida += valor

    def quitação(self):
        if self.saldo > self.divida:
            self.saldo -= self.divida
            self.divida = 0
        else:
            self.divida -= self.saldo
            self.saldo = 0

class Funcionario:
    def __init__(self, pessoa, email, senhaDev, salario):
        self.pessoa = pessoa
        self.email = email
        self.senhaDev = senhaDev
        self.salario = int(salario)

    def aumento(self, valor):
        if valor <= 0:
            raise ValueError("O valor do aumento deve ser positivo")
        self.salario += valor

    def redução(self, valor):
        if valor <= 0:
            raise ValueError("O valor da redução deve ser positivo")
        if valor > self.salario:
            raise ValueError("O salario não pode ser inferior a 0")
        self.salario -= valor