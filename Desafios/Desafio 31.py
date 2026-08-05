import time
distancia = int(input('Digite a distancia de sua viagem: '))
if distancia <= 200:
    maior_taxa = distancia * 0.5
    print(f'De acordo com a viagem de {distancia:.0}KM, a corrida custara R${maior_taxa:.2}!')
else:
    print('Analisando...')
    time.sleep(1)
    menor_taxa = distancia * 0.45
    print(f'Prezado cliente, após analise da sua viagem sua distancia é superior a 200KM neste caso você pagara {menor_taxa}')