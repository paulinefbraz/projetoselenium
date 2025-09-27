<h1 align="center">
🤖 Robô de Automação para o AVA Unieuro 🤖
</h1>

<p align="center">
<a href="#-sobre-o-projeto">Sobre</a> •
<a href="#-funcionalidades">Funcionalidades</a> •
<a href="#-guia-de-instalação">Instalação</a> •
<a href="#️-como-executar">Como Usar</a> •
<a href="#️-avisos-importantes">Avisos</a>
</p>

<p align="center">
<img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python Version">
<img src="https://img.shields.io/badge/Selenium-4-green.svg" alt="Selenium Version">
<img src="https://img.shields.io/badge/status-funcional-brightgreen" alt="Status">
</p>

<details>
<summary><strong>📚 Índice Completo</strong></summary>
<ol>
<li><a href="#-sobre-o-projeto">Sobre o Projeto</a></li>
<li><a href="#-funcionalidades">Funcionalidades</a></li>
<li><a href="#-pré-requisitos">Pré-requisitos</a></li>
<li><a href="#-guia-de-instalação">Guia de Instalação</a></li>
<li><a href="#️-configuração-do-script">Configuração do Script</a></li>
<li><a href="#️-como-executar">Como Executar</a></li>
<li><a href="#️-avisos-importantes">Avisos Importantes</a></li>
</ol>
</details>

📖 Sobre o Projeto
Este projeto automatiza o processo de login e download de arquivos da plataforma de Ensino a Distância (EAD) do Unieuro. Criado para simplificar tarefas repetitivas, o robô navega pelo site, encontra a disciplina correta e baixa os materiais de estudo necessários, salvando tudo de forma organizada.

✨ Funcionalidades
✅ Login automático direto na plataforma EAD.

✅ Navegação inteligente até a sala de aula virtual especificada.

✅ Download de arquivos PDF com base no nome.

✅ Organização automática dos arquivos em uma pasta downloads/.

✅ Dois modos de execução:

Visível: Assista ao robô trabalhando em tempo real.

Headless (Oculto): Para execução rápida e em segundo plano.

📋 Pré-requisitos
Antes de começar, garanta que você tenha os seguintes itens instalados em sua máquina:

Python 3.8+

Google Chrome (Navegador)

🚀 Guia de Instalação
Siga estes passos para deixar o robô pronto para uso.

1️⃣ Passo 1: Prepare a Estrutura de Pastas
Crie a estrutura de pastas exatamente como mostrado abaixo. O arquivo chromedriver.exe precisa estar dentro da pasta chromedrive.

/automacao_ava/
|
|-- 📁 chromedrive/
|   |--  chromedriver.exe
|
|-- 📁 downloads/  (será criada automaticamente)
|
|-- 📜 main.py
|-- 📜 requirements.txt
|-- 📜 README.md
2️⃣ Passo 2: Baixe o ChromeDriver
O ChromeDriver é a ponte entre nosso código e o navegador Google Chrome.

Verifique sua versão do Chrome: Vá em Ajuda > Sobre o Google Chrome.

Baixe o driver correspondente: Acesse Chrome for Testing e baixe o chromedriver para win64 da mesma versão do seu navegador.

Extraia o .zip e mova o arquivo chromedriver.exe para a pasta chromedrive.

3️⃣ Passo 3: Instale as Dependências
Crie um arquivo chamado requirements.txt com o conteúdo abaixo:

selenium
Agora, abra o terminal na pasta do projeto e instale o Selenium com o comando:

Bash

pip install -r requirements.txt
⚙️ Configuração do Script
Abra o arquivo main.py e edite as variáveis na seção de configurações com suas informações:

Python

# --- CONFIGURAÇÕES ---
LOGIN = "SEU_LOGIN_AQUI"
SENHA = "SUA_SENHA_AQUI"
NOME_DA_SALA = "NOME_DA_SUA_DISCIPLINA"
NOME_DO_ARQUIVO = "nome_do_arquivo.pdf"

# Confirme se este caminho para o driver está correto
CHROMEDRIVER_PATH = r"C:\Users\aluno\Desktop\automacao_ava\chromedrive\chromedriver.exe"
▶️ Como Executar
Com tudo configurado, abra seu terminal na pasta automacao_ava e use o comando:

Bash

python main.py
Para ver o navegador durante a execução, altere a última parte do código em main.py para headless=False.

⚠️ Avisos Importantes
Manutenção: Se a estrutura do site do AVA mudar, o robô pode precisar de atualizações nos seus "localizadores" (os caminhos para os elementos).

Segurança: Suas credenciais estão salvas em texto puro no script. Mantenha seus arquivos em um local seguro.

<p align="center">

