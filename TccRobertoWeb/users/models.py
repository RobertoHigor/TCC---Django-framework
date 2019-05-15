from django.db import models
from django.contrib.auth.models import User

class Acesso(models.Model):
    usuario_id = models.OneToOneField(User, on_delete=models.CASCADE)
    senhaPorta = models.IntegerField(unique=True)

    def __str__(self):
        return f'{self.usuario_id.username} Acesso'

    #resolver problema de criar acesso automaticamente