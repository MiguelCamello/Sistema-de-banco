from utils import hasher, formatar_telefone

class Funcionario:
    def __init__(self, pessoa_id, banco_id, telefone, emailStaff, senhaStaff, salario):
        self.pessoa_id = pessoa_id
        self.banco_id = banco_id
        self.telefone = formatar_telefone(str(telefone))
        self.emailStaff = emailStaff
        self.senhaStaff_hash = hasher(senhaStaff)
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