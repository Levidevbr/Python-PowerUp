""" num = input('Digite um numero: ')
ultimo_numero = num[-1]
if ultimo_numero in ('0','2','4','6','8'):    --> está e a forma nao matematica
    print('Seu numero é PAR!')
else:
    print('Seu numero é IMPAR!') """



num = int(input('Digite um numero: '))
resultado = num % 2
if resultado == 0:
    print('Seu numero é PAR!')
else:
    print('Seu numero é IMPAR')
