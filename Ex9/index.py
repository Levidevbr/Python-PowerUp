nome = str(input('Digite qual é seu nome? ')).upper().strip()
if nome == 'LEONARDO':
    print('Que nome lindo!')
elif nome == 'MARIA' or nome == 'JOAO' or nome == 'PEDRO':
    print('Seu nome é bem popular!')
else:
    print('Seu nome é normal')
print(f'Tenha um excelente dia {nome}!')