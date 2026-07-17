salario = float(input('Qual é o salario do funcionario? '))
porcentagem = int(input('Qual é a porcentagem do aumento? '))
cal = ((porcentagem / 100) + 1) * salario
print(f'Um funcionario que ganhava R${salario:.2f}, com {porcentagem}% de aumento, passa a receber agora R${cal:.2f} ')
