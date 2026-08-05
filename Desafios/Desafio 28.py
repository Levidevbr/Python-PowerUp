import random
import time
numero_sorteado = random.randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um numero entre 0 a 5. tente adivinhar...')
print('-=-' * 20)
numero = int(input('Em que numero eu pensei? '))
print('Processando...')
time.sleep(2)
if numero == numero_sorteado:
    print('Parabens!!! Você acertou o numero! ')
else:
    print(f'Você errou : ( ... Eu pensei em {numero_sorteado}, tenta mais uma vez! ')