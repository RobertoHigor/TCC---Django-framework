
### TCC-ROBERTO-WEB

Sistema WEB desenvolvido em Django para o cadastro de Usuários e senhas de Acesso para poder abrir a porta inteligente desenvolvida com Arduino. 
A página Web acessa a tabela de registros e mostra quais foram abertas, por quem e quando.

A aplicação Django faz parte do servidor e permite um acesso remoto ao site de diversos dispositivos:
![Diagrama geral do sistema](https://github.com/RobertoHigor/TCC---Django-framework/blob/master/Diagrama geral do projeto.png)
# Criando ambiente virtual
Basta seguir os seguintes passos:

 1. Instalar o pacote **virtualenv** com o comando `pip install virtualenv`. O ambiente virtual irá servir para instalar as bibliotecas.
 > Dependendo da versão, é recomendado já utilizar o `python3 -m pip install virtualenv` para garantir que irá utilizar a versão do pip associada a sua versão do python.
 3. Executar o virtualenv, depenendo do sistema operacional

### Windows
Será criado um arquivo `virtualenv.exe`dentro da pasta Python(versao)/Scripts. Basta executa-lo ou adicionar na variável de ambiente **PATH**
### Linux
No caso do Linux, basta adicionar ao **PATH** da seguinte forma:
1. Abrir o arquivo `/home/usuario/.bashrc` com um editor de texto.
2. Adicionar no final a linha `export PATH="seu-diretorio:$PATH"`, substituindo `seu-diretorio`pelo caminho de instalação do virtualenv (que é mostrado após instalar com o pip).
3. Salve o arquivo e reinicie o terminal.

## Executando o ambiente virtual
Basta digitar no cmd ou terminal o comando virtualenv.
Para criar o ambiente virtual em uma pasta chamada **env** sem as bibliotecas já instaladas, basta utilizar o comando `virtualenv.exe env --no-site-packages`.

Após instalado, deve-se entrar dentro do ambiente virtual.
No caso do **Windows**, basta executar  `env\Scripts\Activate`. 
No caso do **Linux**, basta executar source env/bin/activate
> Sempre que for executar o programa, é necessário ativar o ambiente virtual. Para sair do ambiente virtual basta utilizar o comando deactivate.

# Pré-requisitos para se utilizar o Django

É **necessário** a instalação das bibliotecas seguintes bibliotecas:
* **django (2.2.10)** o Django em si
* **django-crispy-forms (1.7.2)** para formulários mais bonitos
* **psycopg2 (2.8.2)** que é o conector do PostgreSQL
* **pytz (2019.1)** 
* **sqlparse (0.3.0)**

Para instalar nas versões requiridas, pode-se utilizar de 2 opções
####  Opção 1 (Recomendado)
Instalar com o pip através do arquivo **requirements.txt**. Basta utilizar o argumento `-r` fornecendo o nome do arquivo.
 `python3 -m pip install -r requirements.txt`

#### Opção 2
Instalar os pacotes manualmente com o pip
```python
pip install django==2.2.10
pip install django-crispy-forms==1.7.2
pip install psycopg2==2.8.2
pip install sqlparse==0.3.0
pip install pytz==2019.1
```

# Instruções

## Criando o banco de dados

Antes de tudo, esteja utilizando o ambiente virtual para poder executar as configurações do Django.
Siga os passos para criar e configurar o banco de dados.
 1. É necessário criar o **banco de dados** com o nome `faeterj` no próprio postgreSQL. 
 2. Crie as tabelas do banco através do Django com o comando `python manage.py makemigrations`
 3. Execute o comando `python manage.py makemigrations --empty` para gerar uma migração vazia. 
 4. Copie o código do arquivo `__init__.py` e cole no arquivo gerado pelo comando anterior.
> Por limitação do Postgres, o Django não consegue alterar o valor *default* de uma coluna, então é preciso fazer o processo manualmente. 
5. Execute a migração com o `python manage.py migrate`.

O Banco de dados segue o seguinte diagrama (excluindo as tabelas do Django):
![Diagrama da tabela de acesso, usuário e registro](https://github.com/RobertoHigor/TCC---Django-framework/blob/master/Diagrama banco de dados.png)

## Executando o Django

Basta criar o primeiro **superusuário** do sistema com o comando `python manage.py createsuperuser`, digitando o usuario, email e senha quando for requisitado.

Para iniciar o servidor Django, execute python `python manage.py runserver`.

# Sobre o banco de dados

O banco de dados é onde será armazenado as senhas dos usuários além dos registros de entrada.
 A criação das tabelas do banco de dados é feita pelo Django utilizando a ORM com as classes já construídas.
 É necessário que o PosgreSQL esteja sendo executado. A versão utilizada no projeto foi a `11.3-1`

# Deploy do servidor

>Atualmente as variáveis de ambiente também devem ser colocadas nos arquivos wsgi.

Utilize as configurações do arquivo [httpd-vhosts.conf](https://github.com/RobertoHigor/TCC---Django-framework/blob/master/TccRobertoWeb/TccRobertoWeb/httpd-vhosts.conf) e altere caso seja necessário
No caso do **linux**, o arquivo deve ser colocado no diretório `wamp\bin\apache\apache*versão]\conf\extra`, substituindo o arquivo `httpd-vhosts.conf` que já se encontra nela.

>O Arquivo **vhosts** serve para configurar o **acesso as pastas do site**, incluindo a pasta **static** geral onde se encontra os arquivos javascript, css, mídias entre outros.
>Caso ocorra algum problema (como por exemplo, algum visual do site não funcionar, pode-se gerar novamente o static do Django com o comando `python manage.py collectstatic`
>A pasta static está configurada no `settings.py`, sendo necessário utilizar a tag `{% load static %}` para que o Django carregue automaticamente a pasta criada anteriormente.

Em seguida, é necessário editar os arquivos wsgi dependendo do sistema operacional:

### Windows 
Basta editar o arquivo `wsgi_windows.py` e incluir as variáveis de ambiente no servidor.

### Linux 
 Basta editar o arquivo `wsgi.py` que é gerado pelo próprio Django e incluir as variaǘeis de ambiente.
 Para incluir as variáveis no servidor, basta utilizar o comando `setx` 
 **exemplo**: `setx DB_PASS "Senha do banco". 
 




