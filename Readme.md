## Objetivo
Automatizar o processo de deploy do código puxando o código do github e fazendo o deploy dentroda EC2

## Pré requisitos
python 3.10
pip3
virtualenv
AWS CLI
Jenkins
Java

## Instalando o Jenkins
Para instalar o jenkins na máquina siga os seguintes passos:
    sudo apt-get update -y
    wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key add -
    sudo sh -c 'echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
    sudo apt update
    sudo apt install default-jdk
    sudo apt install default-jre
    sudo apt install jenkins -y
    sudo systemctl start jenkins
    sudo systemctl status jenkins
    sudo ufw allow 8080
    sudo ufw allow OpenSSH
    sudo ufw enable
    sudo ufw status
    Confira se sua EC2 permite a entrada da porta 8080, caso não permita: EC2 -> Segurança -> Grupo de Segurança -> Editar Regras de Entrada

## Configuração do jenkins
Para que tenha privilégios de usuário root e não precise de senha:
	sudo vi  /etc/sudoers
	jenkins ALL=(ALL) NOPASSWD: ALL
	Aperte ESC digite :wq e aperte Enter

Para acessar o jenkins no navegador digite o seu ipv4 público seguido de ":8080", dessa forma:
    https://ec2-public-ipv4:8080

Volte na EC2 e pegue sua senha digitando:
    sudo cat /var/lib/jenkins/secrets/initialAdminPassword

## Criando webhook no github
No seu repositório:
    Vá em Settings -> Webhooks -> Add webhook
    Em 'Payload URL' coloque: http:/{SEU IPV4}/github-webhook/
    Em 'Content Type' selecione application/json
    Em 'Which events would you like to trigger this webhook?' selecione: Let me select individual events. e marque Pushes e Pull requests

## Criando pipeline 
Vá em Novo item no Dashboard
Escolha a opção pipeline
Em General escolha GitHub Project e coloque o link do seu repositorio (https://github.com/usuario/repositorio)
Em Build Triggers selecione GitHub hook trigger for GITScm polling
Em Pipeline selecione Pipeline from SCM -> SCM Git -> Repository URL
Insira o link do seu repositório juntamente com o seu token, dessa forma: https://token@github.com/usuario/repositorio.git
Caso não tenha um token: Perfil Github -> Settings -> Developer settings -> Personal Access Tokens. Ao gerar seu PAT, salve em algum lugar pois ele não poderá mais ser visto
Em Credentials: none
Em Branch specifier: **
Em Script path: coloque o caminho para onde está o seu jenkinsfile
Desative Lightweight checkout

## Jenkinsfile
Executa os seguintes passos:
**Checkout SCM.** Faz o pull do repositório para a EC2(configurado no próprio jenkins)
**Build.** Cria o ambiente e instala as dependências necessárias
**Deploy.** Executa o código na EC2 a partir do main.py
**Sync.** Faz a sincronização do arquivo com os tweets gerado com o bucket s3

## Notas
1 - Altere as chaves de acesso à API para as suas chaves, no arquivo Tokens, localizado no caminho ‘./twitter/Tokens.py’.

2 - Crie um ambiente virtual e instale o requirements.txt dentro dele com o comando pip install -r requirements.txt

3 - Foi utilizado o plugin Pipeline: AWS Steps para configurar uma credencial com as AWS keys, então basta ir ao Jenkinsfile, na parte "withAWS(credentials: 'aws-credentials')" do Stage 'Sync' e colocar suas chaves registradas no jenkins.



