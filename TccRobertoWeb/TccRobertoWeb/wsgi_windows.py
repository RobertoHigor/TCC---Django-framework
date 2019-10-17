import os, sys, site
from django.core.exceptions import ImproperlyConfigured

# Tratando erros de variáveis de ambiente
def get_env_variable(var_name):
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the %s environment variable" % var_name
        raise ImproperlyConfigured(error_msg)

# Adicionar o activate_this do virtualenv
activate_this = 'C:/Users/SirLab/Roberto/tcc-roberto-web/env/Scripts/activate_this.py'

exec(open(activate_this).read(),dict(__file__=activate_this))

# Adicionar o site-packages do virtualenv
site.addsitedir('C:/Users/SirLab/Roberto/tcc-roberto-web/env/Lib/site-packages')

# Adicionar os diretórios da alpicação para o PYTHONPATH
sys.path.append('C:/Users/SirLab/Roberto/tcc-roberto-web/TccRobertoWeb')
sys.path.append('C:/Users/SirLab/Roberto/tcc-roberto-web/TccRobertoWeb/monitoramento')
sys.path.append('C:/Users/SirLab/Roberto/tcc-roberto-web/TccRobertoWeb/users')

# Pegando as variáveis de ambiente e enviando para o Django
os.environ['DJANGO_SETTINGS_MODULE'] = 'TccRobertoWeb.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TccRobertoWeb.settings')
os.environ['ENV_ROLE'] = 'INSERIR ROLE'
os.environ['SECRET_KEY'] = 'INSERIR SECRET KEY'
os.environ['DB_PASS'] = 'INSERIR SENHA DO BANCO DE DADOS'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
