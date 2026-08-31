import random
lista = [0,1,2,3,4,5,6,7,8,9,10]
tentativa = 1

aleatorio = random.choice(lista)

print("Sou seu computador...")
print("Acabei de pensar um numero de 0 a 10")
print("Será que você consegue adivinhar???")

usuario = int(input("Qual é seu palpite? "))

while aleatorio != usuario:
    tentativa += 1
    if usuario > aleatorio:
        usuario = int(input("Digite um valor menor... Tente novamente! "))
    elif usuario < aleatorio:
        usuario = int(input("Digite um valor maior... Tente novamente! "))
else:
    print(f"Parabens você acertou o numero sorteado({aleatorio})! ")
    print(f"Foi necessario {tentativa} para acertar!")