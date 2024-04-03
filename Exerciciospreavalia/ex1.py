import random

randomi = random.randint(1,100)
numero = int

while True:
    numero = int(input("Digite um numero de 1 a 100: "))

    if numero > randomi:
        print("Esse número é maior que o número randômico")
    elif numero < randomi:
        print("Esse número é menor que o número randômico")
    else :
        print(f"Esse é o número escolhido, {randomi}")
        break