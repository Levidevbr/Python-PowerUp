preco = float(input('Qual é o preço do produto? '))
desconto = int(input('Qual é o desconto em %? '))
cal1 = preco - (preco * desconto / 100)
print(f'O produto que custava R${preco:.2f}, na promoção com o desconto de {desconto}%, vai custar R${cal1:.2f}')