valor_compra = float(input("Digite o valor da compra: "))


if valor_compra >= 0.01 and valor_compra <= 9.99:
    desconto = 0
elif valor_compra >= 10.00 and valor_compra <= 99.99:
    desconto = 5
elif valor_compra >= 100.00 and valor_compra <= 499.99:
    desconto = 10
else:
    desconto = 15


valor_final = valor_compra - (valor_compra * desconto / 100)


print(f"Valor da compra: R${valor_compra:.2f}")
print(f"Desconto: {desconto}%")
print(f"Valor final: R${valor_final:.2f}")