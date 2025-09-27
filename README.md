Guia de Instalação e Uso do Robô de Automação do AVA
Olá! Este guia vai te ajudar a configurar e usar o robô que baixa arquivos do AVA Unieuro automaticamente. Siga cada passo com atenção.

Fase 1: Instalar os Programas Necessários
Você só precisa fazer isso uma vez.

Passo 1: Instalar o Navegador Google Chrome
Se você ainda não tem o Google Chrome no seu computador, baixe e instale-o a partir deste link:

https://www.google.com/chrome/

Passo 2: Instalar o Python (O Cérebro do Robô)
O Python é a linguagem de programação que faz o robô funcionar.

Vá para o site oficial do Python: https://www.python.org/downloads/

Clique no botão amarelo para baixar a versão mais recente para Windows.

Execute o instalador que você baixou. Atenção: Na primeira tela do instalador, marque a caixa que diz "Add Python to PATH" no canto inferior esquerdo. Isso é muito importante!

Depois de marcar a caixa, clique em Install Now e siga as instruções até o final.

Fase 2: Preparar a Pasta do Projeto
Agora vamos organizar os arquivos do robô.

Passo 3: Criar a Pasta Principal

Vá para a sua Área de Trabalho (Desktop).

Clique com o botão direito, vá em Novo > Pasta.

Dê à pasta o nome de Robo_AVA. Todos os nossos arquivos ficarão aqui dentro.

Passo 4: Baixar o "Motorista" do Chrome (ChromeDriver)
Este programa permite que o Python controle o Google Chrome.

Abra o Google Chrome, clique nos três pontinhos (⋮) no canto superior direito, vá em Ajuda > Sobre o Google Chrome e anote a versão do seu navegador (ex: 129.0.6666.123).

Acesse o site oficial do ChromeDriver: https://googlechromelabs.github.io/chrome-for-testing/

Na seção Stable, encontre a linha com a mesma versão do seu Chrome.

Clique no link do chromedriver para win64. Um arquivo .zip será baixado.

Abra o arquivo .zip baixado, copie o arquivo chromedriver.exe de dentro dele e cole-o diretamente na sua pasta Robo_AVA.

Passo 5: Criar o Arquivo do Robô (main.py)

Abra a pasta Robo_AVA.

Clique com o botão direito, vá em Novo > Documento de Texto.

Renomeie o arquivo para main.py (apague o .txt do final). O Windows pode perguntar se você tem certeza; clique em "Sim".

Clique com o botão direito sobre o main.py e escolha Editar (ou Abrir com > Bloco de Notas).

Copie todo o código abaixo e cole-o no Bloco de Notas.

Python

# Insira aqui o código Python completo que eu forneci na resposta anterior.
# O código que começa com "import os" e termina com "main()".
# É o mesmo código que funcionou para você.
Edite as suas informações! Altere as linhas de LOGIN, SENHA, etc., com os dados corretos.

SALVE O ARQUIVO (Ctrl + S) e feche o Bloco de Notas.

Passo 6: Criar o Arquivo de Dependências (requirements.txt)

Na pasta Robo_AVA, crie outro Documento de Texto.

Renomeie-o para requirements.txt.

Abra-o com o Bloco de Notas, escreva a palavra selenium dentro dele, salve e feche.

Ao final desta fase, sua pasta Robo_AVA deve conter 3 arquivos: chromedriver.exe, main.py, e requirements.txt.

Fase 3: Instalação Final e Execução
Passo 7: Abrir o Terminal na Pasta Certa

Clique na barra de endereço da pasta Robo_AVA (onde aparece C:\Users\SeuNome\Desktop\Robo_AVA).

Apague o texto que está lá, digite cmd e aperte Enter.

Uma tela preta (o terminal) irá abrir, já dentro da pasta correta.

Passo 8: Instalar o Selenium
No terminal que abriu, digite o seguinte comando e aperte Enter:

pip install -r requirements.txt
Espere ele terminar a instalação.

Passo 9: Executar o Robô!
Com tudo pronto, digite o comando abaixo no mesmo terminal e aperte Enter:

python main.py
O robô começará a trabalhar! Se você configurou o headless=False no script, uma janela do Chrome vai abrir. Se não, ele vai rodar em segundo plano.

Passo 10: Verificar o Resultado
Após a execução terminar, uma nova pasta chamada downloads aparecerá dentro da pasta Robo_AVA. O seu arquivo PDF estará lá dentro.

Pronto! Agora a pessoa pode rodar o robô quantas vezes quiser apenas repetindo o Passo 9. Mantenha o arquivo em um local seguro e não o compartilhe publicamente.
