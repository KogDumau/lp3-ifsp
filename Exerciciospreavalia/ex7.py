import random
palavras = ["kogmaw", "ashe", "hasagi", "bergamota", "pindamonhangaba", "kite"]

def escolher_palavra():
  palavra_escolhida = random.choice(palavras)
  return palavra_escolhida

def verificar_letra(palavra, letra):
  if letra in palavra:
    return True
  else:
    return False

def mostrar_palavra(palavra, letras_adivinhadas):
  palavra_com_acertos = ""
  for letra in palavra:
    if letra in letras_adivinhadas:
      palavra_com_acertos += letra
    else:
      palavra_com_acertos += "_"
  return palavra_com_acertos

def jogo_da_forca():
  
  palavra_escolhida = escolher_palavra()
  tentativas = 6
  letras_adivinhadas = []

  while True:
    palavra_com_acertos = mostrar_palavra(palavra_escolhida, letras_adivinhadas)
    print(f"Palavra: {palavra_com_acertos}")
    print(f"Tentativas restantes: {tentativas}")

    letra = input("Digite uma letra: ")

    if letra in letras_adivinhadas:
      print("Essa letra já foi adivinhada!")
      continue

    letras_adivinhadas.append(letra)

    if verificar_letra(palavra_escolhida, letra):
      print("Acertou!")

      if all(letra in letras_adivinhadas for letra in palavra_escolhida):
        print(f"Você venceu! A palavra era {palavra_escolhida}")
        break
    else:
      print("Errou!")
      tentativas -= 1

    if tentativas == 0:
      print(f"Você perdeu! A palavra era {palavra_escolhida}")
      break