sexo = ""

sexo = str(input(f"Digite seu sexo: [M/F] ")).upper().strip()

while sexo not in ("M", "F"):
    sexo = str(input("Digitado incorretamente... por favor digite seu sexo: [M/F] ")).upper().strip()
else:
    print(f"Sexo {sexo} registrado com sucesso!")