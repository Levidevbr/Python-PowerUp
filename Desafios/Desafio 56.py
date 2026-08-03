nomes = []
idades = []
sexos = []
maior_indice = 0
nome_maior = []
sexo_f_menor = 0



for tabela_pessoas in range(1, 5):
    print(f"------ {tabela_pessoas}ª Pessoa ------")
    nome = str(input("Nome: ")).strip().upper()
    nomes.append(nome)
    idade = int(input("Idade: "))
    idades.append(idade)
    sexo = str(input("Sexo [M/F]: ")).strip().upper()
    sexos.append(sexo)
    media = sum(idades) / len(idades)
    if tabela_pessoas == 1:
        maior_indice = idade
        nome_maior = nome
    else:
        if maior_indice < idade:
           maior_indice = idade
           nome_maior = nome
    if idade < 20 and sexo == "F":
        sexo_f_menor += 1



print(f"A média de idade do grupo é de {media:.2f}")
print(f"O homem mais velho tem {maior_indice} anos e se chama {nome_maior}")
print(f"Ao todo são {sexo_f_menor} mulheres com menos de 20 anos")

