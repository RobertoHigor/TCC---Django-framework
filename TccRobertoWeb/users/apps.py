from django.apps import AppConfig


class UserConfig(AppConfig):
    name = 'users'

    #Importando signals
    def ready(self):
        import users.signals

#utilizar signal para criar acesso automaticamente