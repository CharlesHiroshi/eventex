"""
WSGI config for eventex project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
# importa o módulo Cling do pacote dj_static para gerenciar os arquivos estáticos
from dj_static import Cling
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "eventex.settings")

application = Cling(get_wsgi_application())
