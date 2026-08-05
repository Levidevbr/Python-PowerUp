maior = 0
menor = 0


for pessoas in range(1, 6):
    peso = float(input(f"Peso da {pessoas}ª pessoa: "))
    if pessoas == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f"O maior peso informado é {maior:.1f}KG!")
print(f"O menor peso informado é {menor:.1f}KG!")
