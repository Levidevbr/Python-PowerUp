n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1 + n2) / 2
if media >= 6:
    print(f'Sua media é: {media:.1f}')
    print(f'Parabens você passou de ano!')
else:
    print(f'Sua media é: {media:.1f}')
    print(f'Você infelizmente reprovou : ( ')