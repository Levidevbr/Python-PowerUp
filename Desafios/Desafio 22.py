nome = str(input('Digite seu nome completo: ')).strip()
primeiro_nome = nome.split()[0]
letras_reais = nome.replace(' ', '')
print('Analisando seu nome...')
print(f'Seu nome em maiúscula é {nome.upper()}')
print(f'Seu nome minuscula é {nome.lower()}')
print(f'Seu nome tem ao todo {len(letras_reais)} letras')
print(f'Seu primeiro nome é {primeiro_nome} e ele tem {len(primeiro_nome)} letras')