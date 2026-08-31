def hasher(senha):
    senha_hashed=''
    for l in senha:
        senha_hashed += ('#'+l+'@')
    return senha_hashed

def unhasher(senha_hashed):
    senha_normal=''
    for i in senha_hashed:
        if i in '#@':
            continue
        senha_normal += i
    return senha_normal