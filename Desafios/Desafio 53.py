nome = str(input("Digite uma frase: ")).upper().replace(" ", "")

invert = nome[::-1]

print(f"O inverso de {nome} é {invert}")

if nome == invert:
    print("Esta frase é Palíndromo")

else:
    print("Está frase nao é Palíndromo")