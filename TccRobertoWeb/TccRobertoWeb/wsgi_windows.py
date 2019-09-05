"""
WSGI config for TccRobertoWeb project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os
#imports do windows
import sys
import site

#Adicionar o activate_this do virtualenv
activate_this = 'C:/Users/SirLab/Roberto/tcc-roberto-web/env/Scripts/activate_this.py'

exec(open(activate_this).read(),dict(__file__=activate_this))

#Adicionar o site-packages do virtualenv
site.addsitedir('C:/Users/SirLab/Roberto/tcc-roberto-web/env/Lib/site-packages')

#Adicionar os diretórios da alpicação para o PYTHONPATH
sys.path.append('C:/Users/SirLab/Roberto/tcc-roberto-web/TccRobertoWeb')
sys.path.append('C:/Users/SirLab/Roberto/tcc-roberto-web/TccRobertoWeb/monitoramento')
sys.path.append('C:/Users/SirLab/Roberto/tcc-roberto-web/TccRobertoWeb/users')

os.environ['DJANGO_SETTINGS_MODULE'] = 'TccRobertoWeb.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TccRobertoWeb.settings')

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
