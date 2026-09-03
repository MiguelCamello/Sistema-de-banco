from utils import formatar_cpf

class Pessoa:
    def __init__(self, nome, cpf, idade, genero):
        self.nome = nome
        self.cpf = formatar_cpf(str(cpf))
        self.idade = int(idade)
        self.genero = genero
