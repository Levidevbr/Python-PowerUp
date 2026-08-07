import random

lista = [0,1,2,3,4,5,6,7,8,9,10]
jogador = -1
escolhido = random.choice(lista)
tentativa = 0

print("Sou seu computador...")
print("Acabei de pensar em um numero entre 0 a 10.")
print("Será que você consegue adivinhar qual foi?")

while jogador != escolhido:
    jogador = int(input("Qual é seu palpite? "))
    tentativa += 1

    if jogador != escolhido:

        print("Você errou!")

        if jogador < escolhido:
            print("Digite um numero mais alto!")

        elif jogador > escolhido:
            print("Digite um numero mais baixo!")
            
    else:
        print("Você acertou!")
        print(f"Foi necessario {tentativa} jogadas.")