from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Registro(models.Model):
    sala_acesso = models.CharField(max_length=20)
    #Alterado no mysql para TIMESTAMP
    data_acesso = models.DateTimeField(default=timezone.now)
    #Desativando on_delete Cascade para não apagar o registro caso o usuário seja deletado
    usuario = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
