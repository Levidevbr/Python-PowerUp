contador = 1

print("Gerador de PA")
print("-=-"*5)

primeiro_termo = int(input("Primeiro termo: "))
razao = int(input("Razão do PA: "))

while contador <= 10:
    print(primeiro_termo, end=" -> ")
    contador += 1
    primeiro_termo += razao
print(f"{primeiro_termo}")

