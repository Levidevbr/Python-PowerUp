import time
print('Boa tarde!!!')
time.sleep(1)
velocidade = int(input('Qual é a velocidade atual do seu carro? '))
print('ANALISANDO SUA VELOCIDADE...')
time.sleep(2.5)
if velocidade <= 80:
    print('Tenha um bom dia! Continue Dirigindo com segurança!')
else:
    multa = (velocidade - 80) * 7
    print('MULTADO! Você excedeu o limite permitido que é de 80KM/H')
    print(f'Neste caso você deve pagar uma multa de R$ {multa}!')
    print('Tenha um bom dia! Dirija com segurança!')