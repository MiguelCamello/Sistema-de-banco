from utils import hasher

class Usuario:
    def __init__(self, pessoa_id, banco_id, telefone, email, senha):
        self.pessoa_id = pessoa_id
        self.banco_id = banco_id
        self.telefone = telefone
        self.email = email
        self.senha_hash = hasher(senha)
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