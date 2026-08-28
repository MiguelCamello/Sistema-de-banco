from bancos import *
from dados import *

# ==============================
# TESTES
# ==============================

# Pessoas
pessoa1 = Pessoa(
    "Miguel Lima",
    "123.456.789.00",
    20,
    "Masculino",
    "(14)99999-9999"
)

pessoa2 = Pessoa(
    "João Silva",
    "987.654.321.00",
    25,
    "Masculino",
    "(14)98888-8888"
)

pessoa3 = Pessoa(
    "Maria Santos",
    "456.789.123.00",
    32,
    "Feminino",
    "(14)97777-7777"
)

pessoa4 = Pessoa(
    "Ana Oliveira",
    "321.654.987.00",
    28,
    "Feminino",
    "(14)96666-6666"
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


criar_tabela_pessoa()
criar_tabela_usuario()

# salvar_pessoa(pessoa1)
# salvar_pessoa(pessoa2)
# salvar_pessoa(pessoa3)
# salvar_pessoa(pessoa4)


# # buscar_pessoa('12345678900')
# # buscar_pessoa('98765432100')

# # listar_pessoas()

# # deletar_pessoa('98765432100')

# salvar_usuario(usuario1)
# salvar_usuario(usuario2)
# salvar_usuario(usuario3)
# salvar_usuario(usuario4)
buscar_usuario('123.456.789.00')