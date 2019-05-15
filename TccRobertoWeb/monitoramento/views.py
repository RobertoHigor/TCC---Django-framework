from django.shortcuts import render
from django.views.generic import ListView
from .models import Registro

class RegistroListView(ListView):
    model = Registro 
    template_name = 'monitoramento/home.html'
    context_object_name = 'registros'
    #ordering = ['data_acesso']
    paginate_by = 10
    def get_queryset(self):
        try:
            query = self.request.GET.get('q')
        except:
            query = ''
        if query:
            object_list = Registro.objects.filter(sala_acesso__icontains=query).order_by('-data_acesso')
        else:
            object_list = Registro.objects.all().order_by('-data_acesso')
        return object_list
      

def about(request):
     return render(request, 'monitoramento/about.html', {'title': 'About'})