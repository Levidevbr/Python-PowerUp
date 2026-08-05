import datetime

ano = int(input('Qual é o ano do seu nascimento? '))
dt_atual = datetime.date.today().year
idade = dt_atual - ano
tempo_alistamento = idade - 18
dt_alistamento = dt_atual - tempo_alistamento


print(f'Quem nasceu em {ano} tem {idade} em {dt_atual}')

if idade > 18:

    print(f'Você já deveria ter se alistado há {tempo_alistamento} anos atras')
    print(f'Seu alistamento foi em {dt_alistamento}')

elif idade < 18:
    res_alistamento = dt_alistamento - dt_atual

    print(f'Ainda faltam {res_alistamento} anos para o alistamento')
    print(f'Seu alistamento será em {dt_alistamento}')

else:
    print('Você tem que se alistar imediatamente!')