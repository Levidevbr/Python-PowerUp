# Passo 1: Entrar no sistema da empresa (check)
# Passo 2: Fazer login (check)
# Passo 3: Abrir a base de dados
# Passo 4: Cadastrar 1 produto
# Passo 5: Repetir o passo 4 ate acabar a lista de produtos


import pyautogui
import time
import pandas
email = "seu_email@gmail.com"
senha = "sua_senha"
time.PAUSE = 0.5


pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(2)


pyautogui.click(x=257, y=53)
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
time.sleep(3)

pyautogui.click(x=1074, y=402)
pyautogui.write(email)
pyautogui.press('tab')
pyautogui.write(senha)
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(5)

Tabela = pandas.read_csv('Produtos.csv')
print(Tabela)

for linha in Tabela.index:
    pyautogui.click(x=1028, y=293)
    codigo = str(Tabela.loc[linha, 'codigo'])
    pyautogui.write(codigo)
    pyautogui.press('tab')
    marca = str(Tabela.loc[linha, 'marca'])
    pyautogui.write(marca)
    pyautogui.press('tab')
    tipo = str(Tabela.loc[linha, 'tipo'])
    pyautogui.write(tipo)
    pyautogui.press('tab')
    categoria = str(Tabela.loc[linha, 'categoria'])
    pyautogui.write(categoria)
    pyautogui.press('tab')
    preco = str(Tabela.loc[linha, 'preco_unitario'])
    pyautogui.write(preco)
    pyautogui.press('tab')
    custo = str(Tabela.loc[linha, 'custo'])
    pyautogui.write(custo)
    pyautogui.press('tab')
    obs = str(Tabela.loc[linha, 'obs'])
    if pandas.notna(obs):
        pyautogui.write(str(obs))
    pyautogui.press('tab')
    pyautogui.press('enter')

    pyautogui.scroll(5000)




