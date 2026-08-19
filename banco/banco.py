
class Pessoa:
    def __init__(self, nome, idade, genero):
        self.nome = nome
        self.genero = genero
        self.idade = int(idade)

class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []
        self.usuarios = []

    def cadastrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def remover_usuario(self, usuario):
        self.usuarios.remove(usuario)

    def contratar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def demitir_funcionario(self, funcionario):
        self.funcionarios.remove(funcionario)

class Usuario:
    def __init__(self, nome, cpf, telefone, email):
        pass