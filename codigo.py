#Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa
        #https://dlp.hashtagtreinamentos.com/python/intensivao/login
# pip install pyautogui
import pyautogui 
import time

pyautogui.PAUSE = 0.5

# pyautogui.click ~> Clicar em algum lugar da tela
# pyautogui.write ~> escrever um texto
# pyautogui.press ~> pressionar 1 tecla do teclado
# pyautogui.hotkey("crtl, v") ~> combinação

#abrir navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# dar uma pausa um pouco maior (3 segundos)
time.sleep(3)


# Passo 2: Fazer login

pyautogui.click(x=890, y=380)
pyautogui.write("qualqueremail@gmail.com")
#escrever senha
pyautogui.press("tab")
pyautogui.write("minhasenha")

#clicar no botão de logar

pyautogui.click(x=948, y=537)
time.sleep(3)

# Passo 3: Importar base de dados
# pip install pandas numpy openpyxl

import pandas
tabela = pandas.read_csv("produtos.csv")
#tabula leitor de pdf

print(tabela)

# Passo 4: Cadastrar 1 produto
# para cada linha da minha tabela

for linha in tabela.index:

    # clicar no primeiro campo
    pyautogui.click(x=853, y=262)
    # Cadastrar codigo do produto
    codigo = tabela.loc[linha, "codigo"]

    pyautogui.write(codigo)
    pyautogui.press("tab")

    # marca

    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    #tipo
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    #categoria
    # str ~> texto
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    #preço
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    #custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    #obs
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(tabela.loc[linha, "obs"])
    pyautogui.press("tab")

    #enviar
    pyautogui.press("enter")
    pyautogui.scroll(5000)

# Passo 5: Repertir o processo até acabar a base de dados
    
    




#