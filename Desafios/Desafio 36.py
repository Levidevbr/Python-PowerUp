vl_casa = float(input('Digite o valor da casa que deseja comprar R$: '))
salario = float(input('Digite seu salário R$: '))
tmp_pgt = int(input('Digite quantos anos deseja pagar: '))

parcela = vl_casa / (tmp_pgt * 12)
calculo = (salario * 30) / 100

if parcela <= calculo:
    print(f'Para pagar uma casa de R${vl_casa} em {tmp_pgt} anos a prestação será de R$ {parcela:.2f}')
    print('Seu emprestimo foi concedido com SUCESSO!!!')
else:
    print('Seu emprestimo infelizmente foi negado!!!')