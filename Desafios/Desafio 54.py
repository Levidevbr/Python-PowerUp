import datetime

maiores = 0
menores = 0
dt_atual = datetime.date.today().year

for pessoas in range(1, 8):
    idade = int(input(f"Em que ano a {pessoas}ª pessoa nasceu? "))
    valid_idade = dt_atual - idade
    if valid_idade >= 18:
        maiores += 1
    else:
        menores += 1

print(f"Ao todo tivemos {menores} pessoas menor de idade!")


print(f"E tambem tivemos {maiores} pesoas maiores de idade!")

