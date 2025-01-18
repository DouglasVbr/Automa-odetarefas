# abrir o sistema da empressa 
 
import pyautogui

import time

pyautogui.PAUSE = 0.5
#pyautogui.click 
#pyautogui.press 
#pyautogui.write

# abrir o sistema: https://dlp.hastagtreinamentos.com/python/intersivao/login

# fazer o login 

# importar a base de dados 

# cadastrar 1 produto 

# repetir para cada produto

pyautogui.press("win")

pyautogui.write("chrome")

pyautogui.press("enter")

pyautogui.write("https://dlp.hastagtreinamentos.com/python/intersivao/login")

pyautogui.press("enter")

time.sleep(3)

pyautogui.click(x=695, y=462)

pyautogui.write("douglascanal1998@gmail.com")

pyautogui.press("tab")

pyautogui.write("Iaomiofaile06!")

pyautogui.press("tab")

pyautogui.press("enter")

time.sleep(3)

import pandas

tabela = pandas.read.csv("produtos.csv")

print(tabela)


time.sleep(3)



for linha in tabela.index:

    pyautogui.click(x=657, y=332)

    # codigo

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")

    # marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")


    # tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")


    # categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")


    # preco_unitario
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")

    # custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    # obs
    obs = tabela.loc[linha, "obs"]
if obs != "nan ":
    pyautogui.write(str(obs))
pyautogui.press("tab")

time.sleep(3)

pyautogui.press("enter")

    # numero positivo scroll pra cima numero negativo scroll para baixo
pyautogui.scroll(10000)











