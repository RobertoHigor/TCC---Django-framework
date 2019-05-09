from django.shortcuts import render
from django.views.generic import ListView

class RegistroListView(ListView):
    model = Registro 
    template_name = 'monitoramento/home.html'
    context_object_name = 'registros'
    ordering = ['-data_acesso']
    paginate_by = 10