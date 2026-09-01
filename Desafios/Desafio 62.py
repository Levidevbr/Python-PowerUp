contador = 0

print("Gerador de PA")
print("-=-"*10)
termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão do PA: "))

while contador < 10:
    print(termo, end=" -> ")
    termo += razao
    contador += 1

print("PAUSA")

nova_pa = int(input("Quantos termos você quer mostrar a mais?: "))

while nova_pa != 0:

    contador_extra = 0

    while nova_pa > contador_extra:
        print(termo, end=" -> ")
        termo += razao
        contador_extra += 1

    print("PAUSA")

    nova_pa = int(input("Quantos termos você quer mostrar a mais?: "))

print("FIM!")

