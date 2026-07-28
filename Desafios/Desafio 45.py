import time
import random

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

if jogada == aleatorio:
    print('houve um empate!')

elif jogada == 0 and aleatorio == 1:
    print(f'MAQUINA VENCEU com PAPEL!')

elif jogada == 0 and aleatorio == 2:
    print('JOGADOR VENCEU com PEDRA!')

elif jogada == 1 and aleatorio == 0:
    print(f'JOGADOR VENCEU com PAPEL!')

elif jogada == 1 and aleatorio == 2:
        print(f'MAQUINA VENCEU com TESOURA!')

elif jogada == 2 and aleatorio == 0:
    print(f'MAQUINA VENCEU com PEDRA!')

elif jogada == 2 and aleatorio == 1:
    print(f'JOGADOR VENCEU com TESOURA!')

else:
    print('FAVOR DIGITAR UMA OPÇÃO VALIDA!')
