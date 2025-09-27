import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# --- CONFIGURAÇÕES ---
LOGIN = "05796056123"
SENHA = "05796056123"
NOME_DA_SALA = "24 | GPSINN | PROJETO INTEGRADOR DE SISTEMAS COMPUTACIONAIS"
NOME_DO_ARQUIVO = "globo.pdf"
# O caminho correto para o seu chromedriver
CHROMEDRIVER_PATH = r"C:\Users\aluno\Desktop\automacao_ava\chromedrive\chromedriver.exe"

def create_driver(headless=True):
    """Configura e inicializa o driver do Chrome."""
    print("Configurando as opções do Chrome...")
    
    # --- CONFIGURAÇÃO DO DOWNLOAD ---
    caminho_do_projeto = os.path.dirname(os.path.realpath(__file__))
    pasta_de_download = os.path.join(caminho_do_projeto, "downloads")
    if not os.path.exists(pasta_de_download):
        os.makedirs(pasta_de_download)
    print(f"Os arquivos serão baixados em: {pasta_de_download}")

    chrome_options = Options()
    if headless:
        print("Executando em modo headless (segundo plano).")
        chrome_options.add_argument("--headless")
    else:
        print("Executando em modo visível (com navegador).")
    
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": pasta_de_download,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "plugins.always_open_pdf_externally": True
    })

    print("Inicializando o navegador...")
    if not os.path.exists(CHROMEDRIVER_PATH):
        raise FileNotFoundError(f"ChromeDriver não encontrado em: {CHROMEDRIVER_PATH}")
        
    service = Service(executable_path=CHROMEDRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

def main():
    """Função principal para executar a automação."""
    # ==================== ALTERAÇÃO SOLICITADA ====================
    # Trocado para False para que a janela do navegador seja exibida.
    driver = create_driver(headless=False)
    # =============================================================
    
    wait = WebDriverWait(driver, 30)

    try:
        # 1. Acessar a página de login direto
        print("Acessando a página de login direto do UNIEURO...")
        driver.get("https://ead.unieuro.edu.br/login/index.php")
        
        # 2. Preencher login e senha
        print("Preenchendo informações de login...")
        campo_login = wait.until(EC.visibility_of_element_located((By.ID, "username")))
        campo_login.send_keys(LOGIN)

        campo_senha = driver.find_element(By.ID, "password")
        campo_senha.send_keys(SENHA)

        # 3. Clicar para fazer o login
        print("Realizando login...")
        botao_login = driver.find_element(By.ID, "loginbtn")
        botao_login.click()
        print("Login realizado com sucesso!")

        # 4. Procurar e clicar na sala/curso
        print(f"Procurando a sala: '{NOME_DA_SALA}'...")
        link_da_sala = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "PROJETO INTEGRADOR DE SISTEMAS")))
        link_da_sala.click()

        # 5. Procurar o arquivo PDF e clicar para baixar
        print(f"Procurando o arquivo '{NOME_DO_ARQUIVO}' na sala...")
        link_do_pdf = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, NOME_DO_ARQUIVO)))
        link_do_pdf.click()

        # 6. Esperar o download ser concluído
        print(f"Iniciando download de '{NOME_DO_ARQUIVO}'. Aguardando 5 segundos...")
        time.sleep(5)

        print("Download concluído com sucesso!")

    except TimeoutException as e:
        print("\nERRO: O tempo de espera por um elemento esgotou.")
        nome_arquivo_erro = "erro_screenshot.png"
        driver.save_screenshot(nome_arquivo_erro)
        print(f"Uma imagem do erro foi salva como '{nome_arquivo_erro}'.")
        raise e

    finally:
        # 7. Fechar o navegador ao final de tudo
        print("Processo finalizado. Fechando o navegador.")
        driver.quit()

# Ponto de entrada do script
if __name__ == "__main__":
    main()