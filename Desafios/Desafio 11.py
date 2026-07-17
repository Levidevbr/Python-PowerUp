largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = largura * altura
tinta = area / 2
print(f'Sua parede tem a dimensão de {largura:.2f} x {altura:.2f} e sua área é de {area}m².')
print(f'Para pintar essa parede, você precisará de {tinta:.2f}l de tinta.')

