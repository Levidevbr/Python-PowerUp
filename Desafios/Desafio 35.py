print('-=-' * 10)
print('Analisador de triangulos')
print('-=-' * 10)
primeiro_segmento = float(input('Primeiro segmento: '))
segundo_segmento = float(input('Segundo segmento: '))
terceiro_segmento = float(input('Terceiro segmento: '))
if primeiro_segmento < (segundo_segmento + terceiro_segmento):
    print('Os segmentos acima PODEM FORMAR triangulo')
else:
    print('Os segmentos acima NÃO FORMAR triangulo')
