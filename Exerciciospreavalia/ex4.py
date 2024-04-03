candidato1 = 0
candidato2 = 0
candidato3 = 0


for candidatos in range(0, 3):

    print('vote : candidato1\n')
    print('vote : candidato2\n')
    print('vote : candidato\n')

    voto = str(input('vote em um dos candidatos: '))


    match voto:
        case 'candidato1' :
            candidato1 += 1
        case 'candidato2' :
            candidato2 += 1
        case 'candidato' :
            candidato3 += 1
        case _:
            print('candidato inválido')
            break

print(f'candidato 1 = {candidato1}')
print(f'candidato 2 = {candidato2}')
print(f'candidato 3 = {candidato3}')
    