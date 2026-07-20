dias = int(input('Quantos dias o carro ficou alugado? '))
km = int(input('Quantos KM o carro foi rodado? '))
cal = (dias * 60) + (km * 0.15)
print(f'O total a pagar pelos dias alocados é R$ {cal:.2f}')

