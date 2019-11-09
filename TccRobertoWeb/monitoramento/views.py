from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Registro
from django.contrib.auth.models import User

class RegistroListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = "auth.change_user"
    model = Registro 
    template_name = 'monitoramento/home.html'
    context_object_name = 'registros'
    #ordering = ['data_acesso']
    paginate_by = 10

    #Método para busca por sala
    def get_queryset(self):
        try:
            query = self.request.GET.get('q')
        except:
            query = ''
        if query:
            #Pegando o id dos usuários que possuem os caracteres digitados no nome
            user_list = User.objects.filter(first_name__icontains=query).values('id') 
            #Pegando do banco os registros onde o atributo usuario está contido no user_list
            object_list = Registro.objects.filter(usuario__in=user_list).order_by('-data_acesso')
        else:
            object_list = Registro.objects.all().order_by('-data_acesso')
        return object_list
      

def about(request):
     return render(request, 'monitoramento/about.html', {'title': 'About'})

def acesso(request):
    return render(request, 'monitoramento/acesso.html', {'title': 'Acesso'})