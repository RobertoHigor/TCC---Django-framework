# TCC-ROBERTO-WEB

Sistema WEB desenvolvido em Django para o cadastro de Usuários e senhas de Acesso para poder abrir a porta inteligente desenvolvida com Arduino. A página Web acessa a tabela de registros e mostra quais foram abertas, por quem e quando.

# Pré-requisitos

pip install django
pip install django-crispy-forms
pip install psycopg2

# Instruções

Execute o comando python migrate.py makemigrations para criar o banco de dados. 

Deve-se então criar um superusuário com o comando python manage.py createsuperuser

Para iniciar o servidor, execute python manage.py runserver.

Para criar um acesso para o usuário, basta acessar a página de admin em localhost:8000/admin e criar um novo acesso associado ao usuário criado

Para executar o servidor, deve-se executar o comando python migrate.py runserver
