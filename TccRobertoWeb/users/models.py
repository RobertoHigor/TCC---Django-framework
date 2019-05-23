from django.db import models
from django.contrib.auth.models import User

#Gerar uma senha de 6 digitos.
#O motivo por optar pela senha ser gerada é como a senha é unica, ao receber um erro de "senha existente", a pessoa que está realizando o cadastro irá descobrir uma senha de outro usuário.
def gerarAcesso():  
    # Generate ID once, then check the db. If exists, keep trying.
    senhaPorta = User.objects.make_random_password(length=6, allowed_chars='123456789')
    while Acesso.objects.filter(senhaPorta=senhaPorta).exists():
        senhaPorta = User.objects.make_random_password(length=6, allowed_chars='123456789')
    return int(senhaPorta)
       
class Acesso(models.Model):
    usuario_id = models.OneToOneField(User, on_delete=models.CASCADE)
    senhaPorta = models.IntegerField(unique=True, default = gerarAcesso)

    def __str__(self):
        return f'{self.usuario_id.username} Acesso'
