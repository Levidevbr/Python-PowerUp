peso = float(input('Qual é seu peso? (KG) '))
altura = float(input('Qual é sua altura? (M) '))
imc = peso / (altura ** 2)

print(f'O IMC dessa pessoal é {imc:.1f}, você se encontra ', end="")

if imc < 18.5:
    print('a ABAIXO DO PESO, cuidado!')

elif imc <= 25:
    print('no PESO IDEAL!')

elif imc <= 30:
    print('SOBREPESO, cuidado!')

elif imc <= 40:
    print('em OBESIDADE, cuidado!')

else:
    print('em OBESIDADE MORBIDA, cuidado!')