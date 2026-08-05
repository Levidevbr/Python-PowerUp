numero = int(input('Digite um numero: '))

contador = 0


for divisores in range(1, numero + 1):
    if numero % divisores == 0:
        contador += 1
        print(f"{divisores}", end=" ")

print()

if contador == 2:
    print("Ele é primo")

else:
    print("Ele não é primo")

print(f"O numero {numero} foi divisivel {contador} vezes")