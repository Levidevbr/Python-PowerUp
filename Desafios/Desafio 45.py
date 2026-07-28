import time
import random

pedra = 0
papel = 1
tesoura = 2
aleatorio = random.randint(0,2)

print('Suas opções: ')
print('[ 0 ] PEDRA')
print('[ 1 ] PAPEL')
print('[ 2 ] TESOURA')


jogada = int(input('Qual é sua jogada? '))

print('JO')
time.sleep(0.5)
print('KEN')
time.sleep(0.5)
print('PO!!!')

if jogada == 0:
