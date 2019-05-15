from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Registro(models.Model):
    sala_acesso = models.CharField(max_length=20)
    #Alterado no mysql para TIMESTAMP
    data_acesso = models.DateTimeField(default=timezone.now)
    #Desativando on_delete Cascade
    usuario = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)