import math
angulo = int(input('Digite o angulo que você deseja: '))
conversão = math.radians(angulo)
seno = math.sin(conversão)
cosseno = math.cos(conversão)
tangente = math.tan(conversão)

print(f'O angulo de {angulo} tem SENO de {seno:.2f}')
print(f'O angulo de {angulo} tem COSSENO de {cosseno:.2f}')
print(f'O angulo de {angulo} tem TANGENTE de {tangente:.2f}')