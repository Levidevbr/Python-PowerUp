num = int(input('Digite um numero para ver sua Tabuada: '))

for tabu in range(1, 11):
    calc = num * tabu
    print(f'{num} x {tabu} = {calc}')