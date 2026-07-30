import time

termo = 0

print('=' * 20)
print(f'{"10 TERMOS DE UMA PA":^20}')
print('=' * 20)

time.sleep(1)

termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

print(f'{termo}', end='')

for contador in range(1, 10):
    termo += razao
    print(f' -> {termo}', end='')
