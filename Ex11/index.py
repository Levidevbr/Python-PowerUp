n = 1
par = 0
impar = 0
while n != 0:
    n += 1
    n = int(input('Digite um numero: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print("FIM!")
print(f"Analisando os numeros digitados verificamos que houve {par} pares e {impar} impares.")