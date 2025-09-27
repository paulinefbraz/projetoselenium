# projetoselenium
📖 Descrição
Este projeto é um script de automação desenvolvido em Python com a biblioteca Selenium. Seu objetivo é automatizar a tarefa repetitiva de acessar o Ambiente Virtual de Aprendizagem (AVA) do Unieuro, navegar até uma disciplina específica e realizar o download de um arquivo PDF pré-determinado.

O robô economiza tempo e simplifica o acesso a materiais de estudo recorrentes.

✨ Funcionalidades
Acessa diretamente a página de login do EAD Unieuro.

Realiza o login de forma automática com as credenciais fornecidas.

Navega até a disciplina (sala) especificada.

Localiza um arquivo PDF pelo nome e inicia o download.

Salva o arquivo baixado em uma pasta local downloads/.

Pode ser executado de forma visível (mostrando o navegador) ou em modo headless (em segundo plano, para maior velocidade).

🔧 Pré-requisitos
Antes de começar, garanta que você tenha os seguintes itens instalados:

Python 3.8 ou superior: Baixar Python

Google Chrome: O navegador precisa estar instalado na sua máquina.

ChromeDriver: O driver correspondente à sua versão do Google Chrome.

🚀 Instalação e Configuração
Siga os passos abaixo para preparar o ambiente e rodar o robô.

1. Clone ou baixe este projeto:

Bash

# Se estiver usando Git
git clone <url-do-repositorio>
cd automacao_ava
Ou simplesmente use a pasta automacao_ava que você já tem.

2. Crie um arquivo requirements.txt:
Na pasta do projeto, crie um arquivo chamado requirements.txt e adicione a seguinte linha:

selenium
3. Instale as dependências:
Abra o terminal na pasta do projeto e execute o comando:

Bash

pip install -r requirements.txt
4. Baixe e posicione o ChromeDriver:

Verifique a versão do seu Google Chrome (Ajuda > Sobre o Google Chrome).

Baixe a versão correspondente do ChromeDriver em Chrome for Testing.

Descompacte o arquivo baixado.

Coloque o arquivo chromedriver.exe dentro da pasta chromedrive, conforme a estrutura abaixo:

/automacao_ava/
|-- /chromedrive/
|   |-- chromedriver.exe
|-- /downloads/
|-- main.py
|-- README.md
|-- requirements.txt
5. Configure o main.py:
Abra o arquivo main.py e edite as seguintes variáveis no topo do arquivo com suas informações:

Python

# --- CONFIGURAÇÕES ---
LOGIN = "SEU_LOGIN_AQUI"
SENHA = "SUA_SENHA_AQUI"
NOME_DA_SALA = "NOME_DA_SUA_DISCIPLINA"
NOME_DO_ARQUIVO = "nome_do_arquivo.pdf"
# Verifique se este caminho está correto para o seu computador
CHROMEDRIVER_PATH = r"C:\Users\aluno\Desktop\automacao_ava\chromedrive\chromedriver.exe"
▶️ Como Usar
Com tudo configurado, abra o terminal na pasta raiz do projeto (automacao_ava) e execute o seguinte comando:

Bash

python main.py
O robô iniciará a execução. Por padrão, ele roda em modo headless (escondido). Para assistir à execução, altere a seguinte linha no final do arquivo main.py:

Python

# Para ver o navegador, mude para False
driver = create_driver(headless=False)
⚠️ Avisos Importantes
Este script foi criado para a estrutura do site do AVA Unieuro na data de sua criação. Se o site sofrer alterações visuais ou estruturais, o robô pode parar de funcionar e precisará de ajustes nos seletores (IDs, XPaths, etc.).

Suas credenciais (login e senha) ficam armazenadas em texto plano no arquivo main.py. Mantenha o arquivo em um local seguro e não o compartilhe publicamente.
