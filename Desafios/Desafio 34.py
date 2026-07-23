salario = float(input('Qual é seu salario hoje? '))
if salario >= 1250:
    menor_aumento = salario * (10 / 100)
    print(f'Seu salario aumentou 10%, segue seu novo salario {salario+menor_aumento:.2f}')
else:
    maior_aumento = salario * (15 / 100)
    print(f'Seu salario aumentou 15%, segue seu novo salario {salario+maior_aumento:.2f}')