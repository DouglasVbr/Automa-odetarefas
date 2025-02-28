import pyautogui
import time
import pandas as pd  # Nome correto da biblioteca

pyautogui.PAUSE = 0.5  # Pequena pausa entre comandos

# Abrir o navegador e acessar o sistema
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

time.sleep(2)  # Tempo para o Chrome abrir

# pyautogui.write("https://dlp.hastagtreinamentos.com/python/intersivao/login")
pyautogui.press("enter")

time.sleep(5)  # Tempo para a página carregar

# Fazer login
pyautogui.click(x=695, y=462)
pyautogui.write("douglascanal1998@gmail.com")
pyautogui.press("tab")
pyautogui.write("Iaomiofaile06!")
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(5)  # Tempo para carregar a página após login

# Importar base de dados
caminho_csv = "Aula 1 - Python PowerUp/produtos.csv"
try:
    tabela = pd.read_csv(caminho_csv)
    print(tabela)
except FileNotFoundError:
    print(f"Erro: Arquivo CSV não encontrado no caminho '{caminho_csv}'")
    exit()  # Encerra o script se o arquivo não for encontrado

time.sleep(3)

# Cadastrar os produtos
for linha in tabela.index:
    pyautogui.click(x=657, y=332)  # Clicar para começar o cadastro

    # Código do produto
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")

    # Marca
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")

    # Tipo
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")

    # Categoria
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    # Preço unitário
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")

    # Custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    # Observações (se não for NaN)
    obs = tabela.loc[linha, "obs"]
    if pd.notna(obs):  # Verifica se o campo não é NaN
        pyautogui.write(str(obs))
    pyautogui.press("tab")

    time.sleep(2)  # Tempo para processar antes de cadastrar

    pyautogui.press("enter")  # Confirma cadastro

    time.sleep(2)  # Aguarda antes de cadastrar o próximo produto

# Scroll para o topo
pyautogui.scroll(10000)

print("Cadastro finalizado com sucesso!")
