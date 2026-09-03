contador = 0
decisao = ""
maior = 0
menor = 0

while decisao != "N":
    valor = int(input("Digite um valor: "))
    contador += 1

    if contador == 1:
        maior = valor
        menor = valor
    else:
        if valor > maior:
            maior = valor

        if valor < menor:
            menor = valor

    decisao = str(input("Quer continuar? [S/N] ")).upper()

    while decisao not in ("S", "N"):
        print("VALOR INFORMADO INCORRETO, DIGITE NOVAMENTE!")
        decisao = str(input("Quer continuar? [S/N] ")).upper()

print("FIM!")
print(f"Você digitou {contador} números!")
print(f"O maior número digitado foi {maior} e o menor valor digitado foi {menor}.")