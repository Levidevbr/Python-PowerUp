contador = 0
soma = 0


valor = int(input("Digite um valor [EXCETO 999 PARA FORÇAR PARADA]: "))

while valor != 999:
    contador += 1
    soma += valor
    valor = int(input("Digite um valor [EXCETO 999 PARA FORÇAR PARADA]: "))
print(f"Você digitou {contador} e a soma entre eles é {soma}")