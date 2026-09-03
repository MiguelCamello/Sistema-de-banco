def hasher(senha):
    senha_hashed = ''
    for l in senha:
        senha_hashed += ('#'+l+'@')
    return senha_hashed


def unhasher(senha_hashed):
    senha_normal = ''
    for i in senha_hashed:
        if i in '#@':
            continue
        senha_normal += i
    return senha_normal

# 000.000.000-00


def formatar_cpf(cpf):
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"


def formatar_telefone(telefone):
    return f"({telefone[:2]}){telefone[2:7]}-{telefone[7:]}"

