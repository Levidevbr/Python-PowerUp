contador = 0
calculo_1 = 0
calculo_2 = 1

print("-=-"*10)
print("Sequencia de Fibonacci")
print("-=-"*10)

termos = int(input("Quantos termos você quer mostrar? "))

while contador < termos:
    print(calculo_1, end=" -> ")
    contador += 1
    resultado = calculo_1 + calculo_2
    calculo_1 = calculo_2
    calculo_2 = resultado
      
print("FIM")
