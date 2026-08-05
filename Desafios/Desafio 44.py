import time

print(f'{" LOJA LEONARDO ":=^40}')
preco = float(input('Preço das compras: R$ '))

time.sleep(1)

print('FORMAS DE PAGAMENTO')
print('[ 1 ] a vista dinheiro/cheque')
print('[ 2 ] a vista no cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
opcao = int(input('Qual é a opção? '))

time.sleep(1)

if opcao == 1:
    avista = preco * 0.90

    print(f'O valor da compra é R$ {preco:.2f} !')
    print(f'A opção selecionada tem um desconto de 10%, sendo assim o valor final é de R$ {avista:.2f} !')

elif opcao == 2:
    cartao = preco * 0.95

    print(f'O valor da compra é R$ {preco:.2f} !')
    print(f'A opção selecionada tem um desconto de 5%, sendo assim o valor final é de R$ {cartao:.2f} !')

elif opcao == 3:

    print(f'O valor da compra é R$ {preco:.2f} !')
    print(f'A opção selecionada não possui desconto e nem juros, sendo assim o valor final é R$ {preco:.2f}')

elif opcao == 4:
    preco_juros = preco * 1.20
    quant_x = int(input('Quantas parcelas? '))

    if quant_x >=3:
        preco_parcela = preco_juros / quant_x

        print(f'O valor da compra é R$ {preco:.2f} !')
        print(f'Cada parcela da sua compra ficara R$ {preco_parcela}!')
        print(f'A opção selecionada possui juros, sendo assim em {quant_x}x valor final é R$ {preco_juros:.2f}')

    else:
        print('INVALIDO! quantidade de parcelas incorreta')


else:
    print('INVALIDO! Selecione uma das 4 OPÇÕES')
