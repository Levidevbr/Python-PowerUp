nome = str(input('Digite uma frase: ')).strip().upper()
letra = str(input('Digite a letra desejada: ')).strip().upper()
quantidade = nome.count(letra)
primeira_posicao = nome.find(letra) + 1
ultima_posicao = nome.rfind(letra) + 1
print(f'A letra {letra} aparece {quantidade} vezes na frase')
print(f'A primeira letra {letra} apareceu na posição {primeira_posicao}')
print(f'A ultima letra {letra} apareceu na posição {ultima_posicao}')
