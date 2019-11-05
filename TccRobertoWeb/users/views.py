from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .forms import UserRegisterForm
from .models import Acesso
from django.contrib.auth.models import User
from django.contrib.auth.decorators import permission_required

#Formulário de registro do django
@permission_required('auth.change_user', raise_exception=True) #Apenas quem possui a permissão de alterar usuários pode realizar o cadastro
def register(request):
    if request.method == 'POST':
        #utilizando form criado que herda de UserCreationForm
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            #Envia o formulário e faz um hash da senha
            form.save()
            username = form.cleaned_data.get('username') #Pegar o username do formulário
            user =  User.objects.filter(username=username).first()
            acesso = Acesso.objects.filter(usuario_id=user).first() #Buscar o acesso associado ao usuário criado para a mensagem
            #Exibe umna notificação com a senha gerada para o usuário
            messages.success(request, f'Sua conta foi criada! Você agora pode efetuar login {acesso.senhaPorta}!')
            return redirect('login')
    else:
            form = UserRegisterForm()
         #Enviando a variável para a página
    return render(request, 'users/register.html', {'form': form})

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST) # Utilizando a biblioteca do próprio Django
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user) #Importante para o usuário não precisar relogar  
            messages.success(request, f'Sua senha foi alterada com sucesso')
            return redirect('site-about') #Redirecionar para a página sobre após alterar a senha
        else:
            messages.error(request, f'Por favor corrija os erros abaxio')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'users/changePassword.html', {'form': form}) #Renderizar o formulário