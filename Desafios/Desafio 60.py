fatorial = 1

numero = int(input("Digite um valor para calcular o fatorial: "))

while numero > 1:
    print(numero, end=" x ")
    fatorial *= numero
    numero -= 1

print(f"1 = {fatorial}")