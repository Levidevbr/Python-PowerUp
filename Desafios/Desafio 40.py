import time

VERDE = '\033[32m'
VERMELHO = '\033[31m'
RESET = '\033[m'

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2

print('Fazendo o calculo de sua media...')
time.sleep(1)

if media < 5:
    print(f'Sua media foi: {media:.2f}')
    print(f'Você foi {VERMELHO}REPROVADO!{RESET}')

elif media >= 5 and media <= 6.9:
    print(f'Sua media foi: {media:.2f}')
    print(f'Você está em RECUPERAÇÃO!')

else:
    print(f'Sua media foi: {media}')
    print(f'Você foi {VERDE}APROVADO{RESET}')