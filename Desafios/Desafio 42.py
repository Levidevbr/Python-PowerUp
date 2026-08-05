p_1 = int(input('Primeiro segmento: '))
p_2 = int(input('Segundo segmento: '))
p_3 = int(input('Terceiro segmento: '))

if p_1 + p_2 > p_3 and p_2 + p_3 > p_1 and p_3 + p_1 > p_2:
    print(f'Os segmentos informados é possivel formar um TRIANGULO ', end='')

    if p_1 == p_2 == p_3:
        print('EQUILATERO!')

    elif p_1 == p_2 or p_1 == p_3 or p_2 == p_3:
        print('ISOSCELES!')

    elif p_1 != p_2 and p_1 != p_3 and p_2 != p_3:
        print('ESCALENO!')
else:
    print('Os segmentos informados não é possivel formar um TRIANGULO ')