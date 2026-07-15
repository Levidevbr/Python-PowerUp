valor =  float(input('Digite uma distancia em metros: '))
cm = valor * 100
mm = valor * 1000
print('A medida de {}m corresponde a {:.0f}cm e {:.0f}mm' .format(valor, cm, mm))