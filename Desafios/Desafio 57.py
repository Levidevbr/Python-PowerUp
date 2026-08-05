sexo = ""

while sexo not in ("M", "F"):
    sexo = input("Por favor digite seu sexo: (M/F) ").upper().strip()[0]
    if sexo not in ("M", "F"):
        print("Sexo invalido! Por favor digite seu sexo: ")

print(f"Sexo {sexo} cadastrado com sucesso!")