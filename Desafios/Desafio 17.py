from math import hypot
oposto = float(input('Digite o comprimento do cateto oposto: '))
adjacente = float(input('Digite o comprimento do cateto adjacente: '))
resultado = hypot(oposto, adjacente)
print(f'A hipotenusa é {resultado:.2f}')