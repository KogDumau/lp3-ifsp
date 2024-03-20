def identificadorFuncionario(id):
    if len(id) != 7:
        return False
    if not f'{id[0]}{id[1]}' == 'BR':
        return False
    if not id[len(id) - 1] == 'X':
        return False
    if not int(id[2:6]):
        return False
    return True

print(identificadorFuncionario('BR0001X'))
    