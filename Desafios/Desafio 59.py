import time

opcao = 0

vl_1 = int(input("Digite seu primeiro valor: "))
vl_2 = int(input("Digite seu segundo valor: "))

time.sleep(1)

while opcao != 5:
    print("[ 1 ] somar")
    print("[ 2 ] multiplicar")
    print("[ 3 ] maior ")
    print("[ 4 ] novos numeros")
    print("[ 5 ] sair")

    opcao = int(input("Escolha uma opção: "))

    time.sleep(1)

    if opcao == 1:
        soma = vl_1 + vl_2
        resultado_soma = soma

        print(f"Resultado da operação de SOMA é {resultado_soma}!")

        time.sleep(1)

    elif opcao == 2:
        multiplicacao = vl_1 * vl_2
        resultado_multiplicacao = multiplicacao

        print(f"Resultado da operação de MULTIPLICAÇÃO é {resultado_multiplicacao}!")
        
        time.sleep(1)

    elif opcao == 3:
        if vl_1 > vl_2:
            maior = vl_1
            print(f"Entre os valores informados o maior é {maior}")
        elif vl_2 > vl_1:
            maior = vl_2
            print(f"Entre os valores informados o maior é {maior}")
        else:
            print("Valores iguais, não há valor maior!")

        time.sleep(1)

    elif opcao == 4:
        vl_1 = int(input("Digite seu primeiro novo valor: "))
        vl_2 = int(input("Digite seu segundo novo valor: "))

        time.sleep(1)

    elif opcao == 5:
        print("Programa encerrado, obrigado!")

    else:
        print("Operação invalida!")
        print("Favor digitar uma das opções existentes!")        