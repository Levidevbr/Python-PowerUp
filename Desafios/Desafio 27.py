nome = str(input('Digite seu nome completo: ')).strip().upper()
palavras = nome.split()
primeira_posicao = palavras[0]
ultima_posicao = palavras[-1]
print('Muito prazer em te Conhecer!')
print(f'Seu primeiro nome é {primeira_posicao}')
print(f'Seu ultimo nome é {ultima_posicao}')