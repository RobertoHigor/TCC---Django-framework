from django.db.models.signals import post_save
from django.contrib.auth.models import User
#Receiver é a função que recebe o sinal e faz algumna tarefa. É utilizado com um decorator
from django.dispatch import receiver
from .models import Acesso

@receiver(post_save, sender=User)
def criar_acesso(sender, instance, created, **kwargs):
    if created:
        Acesso.objects.create(usuario_id=instance)

#Salvar o Acesso toda vez que o objeto User for salvo
@receiver(post_save, sender=User)
def salvar_acesso(sender, instance, **kwargs):
    instance.acesso.save()