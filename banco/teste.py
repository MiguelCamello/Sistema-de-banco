from bancos import *
from dados import *

# ==============================
# TESTES
# ==============================

# Pessoas
pessoa1 = Pessoa(
    "Miguel Lima",
    "12345678900",
    20,
    "Masculino",
    "11999999999"
)

pessoa2 = Pessoa(
    "João Silva",
    "98765432100",
    25,
    "Masculino",
    "11988888888"
)

pessoa3 = Pessoa(
    "Maria Santos",
    "45678912300",
    32,
    "Feminino",
    "11977777777"
)

pessoa4 = Pessoa(
    "Ana Oliveira",
    "32165498700",
    28,
    "Feminino",
    "11966666666"
)


# Usuários
usuario1 = Usuario(
    pessoa1,
    "miguel@email.com",
    "1234"
)

usuario2 = Usuario(
    pessoa2,
    "joao@email.com",
    "5678"
)

usuario3 = Usuario(
    pessoa3,
    "maria@email.com",
    "abcd"
)

usuario4 = Usuario(
    pessoa4,
    "ana@email.com",
    "senha123"
)


# Bancos
banco_do_brasil = Banco("Banco do Brasil")
santander = Banco("Santander")


# Cadastrando usuários
banco_do_brasil.cadastrar_usuario(usuario1)
banco_do_brasil.cadastrar_usuario(usuario2)
banco_do_brasil.cadastrar_usuario(usuario3)

santander.cadastrar_usuario(usuario4)




# salvar_pessoa(pessoa3)

# buscar_pessoa(12345678900)
# buscar_pessoa(98765432100)

#listar_pessoas()

deletar_pessoa(98765432100)