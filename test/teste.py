from models import Pessoa, Usuario, Funcionario, Banco
from  database.pessoas_db import *
from  database.usuarios_db import *
from  database.funcionarios_db import *
from  database.bancos_db import *


# ==============================
#            TESTES
# ==============================

# Pessoas
pessoa1 = Pessoa(
    "Miguel Lima",
    "123.456.789.00",
    20,
    "Masculino",
)

pessoa2 = Pessoa(
    "João Silva",
    "987.654.321.00",
    25,
    "Masculino",
)

pessoa3 = Pessoa(
    "Maria Santos",
    "456.789.123.00",
    32,
    "Feminino",
)

pessoa4 = Pessoa(
    "Ana Oliveira",
    "321.654.987.00",
    28,
    "Feminino",
)


# Usuários
usuario1 = Usuario(
    1,
    "(14)99999-9999",
    "miguel@email.com",
    "1234"
)

usuario2 = Usuario(
    2,
    "(14)98888-8888",
    "joao@email.com",
    "5678"
)

usuario3 = Usuario(
    3,
    "(14)97777-7777",
    "maria@email.com",
    "abcd"
)

usuario4 = Usuario(
    4,
    "(14)96666-6666",
    "ana@email.com",
    "senha123"
)
usuario5 = Usuario(
    4,
    "(14)99899-8780",
    "miguel@gmail.com",
    "#123"
)

# funcionarios

funcionario1 = Funcionario(
    1,
    "dev@gmail",
    "senhaDev",
    1500
)


# Bancos
banco_do_brasil = Banco("Banco do Brasil")
santander = Banco("Santander")


# Cadastrando usuários
banco_do_brasil.cadastrar_usuario(usuario1)
banco_do_brasil.cadastrar_usuario(usuario2)
banco_do_brasil.cadastrar_usuario(usuario3)

santander.cadastrar_usuario(usuario4)

# Contratar funcionarios
santander.contratar_funcionario(funcionario1)




criar_tabela_pessoa()
criar_tabela_usuario()

# salvar_pessoa(pessoa1)
# salvar_pessoa(pessoa2)
# salvar_pessoa(pessoa3)
# salvar_pessoa(pessoa4)

# salvar_usuario(usuario1)
# salvar_usuario(usuario2)
# salvar_usuario(usuario3)
# salvar_usuario(usuario4)
# salvar_usuario(usuario5)

deletar_pessoa('321.654.987.00')

# buscar_pessoa('321.654.987.00')
# buscar_usuario(4)

# listar_pessoas()
# listar_usuario()


# usar 'python -m test.teste' no cmd