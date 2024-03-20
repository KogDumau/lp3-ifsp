peso = float(input('Qual seu peso em Kilogramas?: '))
altura = float(input('Qual a sua altura em Metros?: '))

def pesoo(peso, altura):
    imc = peso / (altura * altura)
    peso_normal = 24.9 * (altura * altura)
    peso_exigido = peso_normal - peso

    if imc < 18.5:
        print(f'Você está abaixo do peso, você precisa ganhar {peso_exigido} Kg.')
    elif imc >= 18.5 and imc <= 24.9:
        print(f'Você está no peso ideal para sua altura.')
    elif imc >= 25.0 and imc <= 29.9:
        print(f'Você está com excesso de peso, você precisa perder {peso_exigido} Kg.')
    elif imc >= 30.0 and imc <= 34.9:
        print(f'Você está com obesidade de classe 1, você precisa perder {peso_exigido} Kg.')
    elif imc >= 35.0 and imc <= 39.9:
        print(f'Você está com obesidade de classe 2, você precisa perder {peso_exigido} Kg.')
    else:
        print(f'Você está com obesidade de classe 3, você precisa perder {peso_exigido} Kg, senão é caxa')

pesoo(peso, altura)