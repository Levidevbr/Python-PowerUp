''' --> SEM IMPORT
usuario = float(input('Digite um numero quebrado: '))
print(f'O valor digitado foi {usuario} e sua porção inteira é {int(usuario)}')
'''

from math import trunc
usuario = float(input('Digite um numero: '))
print(f'O valor digitado foi {usuario} e sua porção inteira é {trunc(usuario)}')