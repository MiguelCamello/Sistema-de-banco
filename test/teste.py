import random

from models.bancos import Banco
from models.pessoas import Pessoa
from models.usuarios import Usuario
from models.funcionarios import Funcionario

from database.bancos_db import (
    criar_tabela_bancos,
    salvar_banco
)

from database.pessoas_db import (
    criar_tabela_pessoas,
    salvar_pessoa
)

from database.usuarios_db import (
    criar_tabela_usuarios,
    salvar_usuario
)

from database.funcionarios_db import (
    criar_tabela_funcionarios,
    salvar_funcionario
)


def criar_tabelas():
    criar_tabela_bancos()
    criar_tabela_pessoas()
    criar_tabela_usuarios()
    criar_tabela_funcionarios()


def gerar_dados(
    quantidade_bancos=5,
    quantidade_pessoas=10,
    quantidade_usuarios=7,
    quantidade_funcionarios=3
):

    # =========================
    # TABELAS
    # =========================

    criar_tabelas()

    # =========================
    # BANCOS
    # =========================

    nomes_bancos = [
        "Banco do Brasil",
        "Santander",
        "Itaú",
        "Bradesco",
        "Nubank",
        "Inter",
        "NGCash"
    ]

    bancos_ids = []

    for nome in nomes_bancos[:quantidade_bancos]:

        banco = Banco(nome)

        banco_id = salvar_banco(banco)

        bancos_ids.append(banco_id)

    print(f"{len(bancos_ids)} bancos criados.")


    # =========================
    # PESSOAS
    # =========================

    nomes = [
        "Miguel",
        "Manoela",
        "Kesia",
        "Perolla",
        "Samuel",
        "Valmir",
        "Enzo",
        "João",
        "Pedro",
        "Lucas",
        "Gabriel",
        "Arthur",
        "Rafael",
        "Gustavo",
        "Felipe",
        "Matheus",
        "Bruno",
        "Daniel",
        "Henrique",
        "Leonardo",
        "André",
        "Carlos",
        "Eduardo",
        "Marcos",
        "Thiago",
        "Victor"
    ]

    sobrenomes = [
        "Aguiar",
        "Vitória",
        "Lima",
        "Camello",
        "Aparecida",
        "Silva",
        "Santos",
        "Oliveira",
        "Souza",
        "Pereira",
        "Costa",
        "Rodrigues",
        "Almeida",
        "Nascimento"
    ]

    generos = [
        "Masculino",
        "Feminino"
    ]

    pessoas_ids = []

    for i in range(quantidade_pessoas):

        nome = f"{random.choice(nomes)} {random.choice(sobrenomes)}"

        # CPF fictício e único
        cpf = f"{10000000000 + i}"

        idade = random.randint(18, 70)

        genero = random.choice(generos)

        pessoa = Pessoa(
            nome,
            cpf,
            idade,
            genero
        )

        pessoa_id = salvar_pessoa(pessoa)

        pessoas_ids.append(pessoa_id)

    print(f"{len(pessoas_ids)} pessoas criadas.")


    # =========================
    # USUÁRIOS
    # =========================

    usuarios_ids = []

    for i in range(quantidade_usuarios):

        pessoa_id = pessoas_ids[i]

        banco_id = random.choice(bancos_ids)

        telefone = f"1499{random.randint(1000000, 9999999)}"

        email = f"usuario{i + 1}@email.com"

        senha = str(random.randint(10000, 99999))

        usuario = Usuario(
            pessoa_id,
            banco_id,
            telefone,
            email,
            senha
        )

        # Coloca alguns valores diferentes
        usuario.saldo = random.randint(0, 10000)
        usuario.divida = random.randint(0, 2000)

        salvar_usuario(usuario)

    print(f"{quantidade_usuarios} usuários criados.")


    # =========================
    # FUNCIONÁRIOS
    # =========================

    for i in range(quantidade_funcionarios):

        # Usamos outras pessoas
        pessoa_id = pessoas_ids[
            quantidade_usuarios + i
        ]

        banco_id = random.choice(bancos_ids)

        telefone = f"1499{random.randint(1000000, 9999999)}"

        email = f"funcionario{i + 1}@banco.com"

        senha = str(random.randint(10000, 99999))

        salario = random.randint(2000, 10000)

        funcionario = Funcionario(
            pessoa_id,
            banco_id,
            telefone,
            email,
            senha,
            salario
        )

        salvar_funcionario(funcionario)

    print(f"{quantidade_funcionarios} funcionários criados.")

    print("\n==============================")
    print("     DADOS GERADOS!")
    print("==============================")

gerar_dados()