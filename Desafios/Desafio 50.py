soma = 0
cont = 0

for lista in range(1,7):
    sequen = int(input('Digite um numero: '))
    if sequen % 2 == 0:
        soma += sequen
        cont += 1
print(f'Você informou {cont} valores pares e a soma deles foi: {soma}')