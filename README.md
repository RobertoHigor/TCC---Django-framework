### TCC-ROBERTO-WEB

Sistema WEB desenvolvido em Django para o cadastro de Usuários e senhas de Acesso para poder abrir a porta inteligente desenvolvida com Arduino. A página Web acessa a tabela de registros e mostra quais foram abertas, por quem e quando.


# Criando ambiente virtual
É necessário instalar o pacote virtualenv para que seja possível criar um ambiente virtual onde será instalado as bibliotecas sem que haja conflito com as já existentes no computador.

Para se instalar o virtualenv baixa digitar o comando `pip install virtualenv`

Após instalado, ele irá criar um arquivo chamado virtualenv.exe na pasta Scripts/ dentro da pasta onde estão instalado o Python, no meu caso por utilizar o Python 3.7 32bits está na pasta Python37-32

Para criar o ambiente virtual, deve-se executar o arquivo virtualenv.exe seguido da pasta onde será armazenado o ambiente virtual (no meu caso foi utilizado uma pasta chamada env dentro da pasta raíz do projeto)

O comando ficou `virtualenv.exe env --no-site-packages` pelo fato do arquivo virtualenv.exe já estar nas variáveis do sistema. O argumento --no-site-packages possibilita uma instalação limpa, sem adicionar os pacotes que já estão instalados no sistema.

Após instalado, deve-se entrar dentro do ambiente virtual criado executando o arquivo activate dentro da pasta Scripts criadas, nesse caso o comando é `env\Scripts\Activate`. Sempre que for executar o programa, é necessário ativar o ambiente virtual. Para sair do ambiente virtual basta utilizar o comando deactivate.

# Pré-requisitos para se utilizar o Django

É necessario a instalação das bibliotecas django (2.2.1), django-crispy-forms (1.7.2), do conector do Postgres psycopg2 (2.8.2), do pytz (2019.1) e opcionalmente do sqlparse (0.3.0)

```
pip install django==2.2.1
pip install django-crispy-forms==1.7.2
pip install psycopg2==2.8.2
pip install sqlparse==0.3.0
pip install pytz==2019.1
```

A lista de bibliotecas se encontra no arquivo `requirements.txt` e podem ser instaladas através do comando `pip intall -r requirements.txt`

## Instruções

# Criando o banco de dados

Primeiro é necessário criar um banco de dados com o nome `faeterj`. Já dentro do ambiente virtual, execute o comando `python manage.py makemigrations` para criar o banco de dados. 

Importante: É gerado um arquivo dentro da pasta migrations dentro da aplição cada vez que o makemigrations executa alguma alteração. Use com cuidado.

Por padrão o Django não altera o valor padrão de uma tabela, para isso é necessário utilizar o comando `python manage.py makemigrations --empty` para gerar uma migration vazia. Pode-se então copiar o código do arquivo `__init__.py` dentro da pasta migrations e colar no arquivo que foi gerado pelo comando.

Após ter criado a migração, é preciso aplica-la utilizando o comando `python manage.py migrate`. Deve-se então criar um superusuário com o comando `python manage.py createsuperuser`

Para iniciar o servidor Django, execute python `python manage.py runserver`.

Para criar um acesso para o usuário dentro do sistema, basta acessar a página de admin em localhost:8000/admin e criar um novo acesso associado ao super usuário criado anteriormente.

## Banco de dados PostgresSQL

O banco de dados é onde será armazenado as senhas dos usuários além dos registros de entrada. A criação do banco de dados será feita pelo Django utilizando a ORM porém é necessário que seja instalado o PostgresSQL para que seja executado o banco de dados.
A versão utilizada foi a 11.3-1

# Como executar
Basta inicializar o serviço, no caso do windows, pode ser feito apertando windows + r e digitando services.msc para localizar e inicalizar o serviço postgresql-x64-11.
O PostgresSQL provém uma interface gráfica pelo aplicativo pgAdmin4.

## Deploy do servidor

Para fazer deploy do servidor, basta configurar o arquivo wsgi_windows.py caso queira hospedar no windows ou editar o arquivo wsgi.py gerado pelo Django caso queira utilizar um servidor linux.
As variáveis de ambiente (Como as senhas e a SECRET_KEY) devem ser configuradas no computador que irá hospedar o servidor através do comando `setx` exemplo: `setx DB_PASS "Senha do banco". *Atualmente elas devem ser postas no arquivo wsgi_windows.py para passar para o Apache

Além disso, é necessário também utilizar a cópia do arquivo vhosts incluida no repositório e configurar caso necessário. Deve ser posta na pasta `wamp\bin\apache\apache(versão)\conf\extra` substituindo o arquivo httpd-vhosts.conf que já se encontra nela.

No arquivo vhosts é onde se configura o acesso as pastas do site, incluindo a static que é onde o Django armazena arquivos como javascript, css e mídias. É recomendado gerar novamente os arquivos static caso ocorra algum problema (Como o site ficar sem css). Isso é feito através do comando `python manage.py collectstatic` onde será gerado uma pasta geral static contendo todos os arquivos do servidor, que deve ser adicionada ao arquivo vhosts para permitir acesso a elas.

Para isso também é necessário utilizar a tag `{% load static %}` para que o Django carregue automaticamente a static da pasta configurada no `settings.py` diminuindo a reescrita de código.
