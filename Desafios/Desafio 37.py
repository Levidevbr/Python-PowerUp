num = int(input('Digite um numero inteiro: '))
print('Escolha uma das bases para conversão: ')
print('[ 1 ] converter para BINÁRIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print(f'{num} convertido em BINARIO é igual a {num:b}')
elif opcao == 2:
    print(f'{num} convertido em OCTAL é igual a {num:o}')
elif opcao == 3:
    print(f'{num} convertido em HEXADECIMAL é  igual a {num:x}')
else:
    print('Ocorreu um erro, favor digitar apenas as opções existentes... (1, 2 ou 3)')