from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from .models import Acesso
from django.contrib.auth.models import User
from django.contrib.auth.decorators import permission_required

#Formulário de registro do django
@permission_required('auth.change_user', raise_exception=True)
def register(request):
    if request.method == 'POST':
        #utilizando form criado que herda de UserCreationForm
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            #Envia o formulário e faz um hash da senha
            form.save()
            username = form.cleaned_data.get('username')
            user =  User.objects.filter(username=username).first()
            acesso = Acesso.objects.filter(usuario_id=user).first()
            messages.success(request, f'Sua conta foi criada! Você agora pode efetuar login {acesso.senhaPorta}!')
            return redirect('login')
    else:
            form = UserRegisterForm()
         #Enviando a variável para a página
    return render(request, 'users/register.html', {'form': form})