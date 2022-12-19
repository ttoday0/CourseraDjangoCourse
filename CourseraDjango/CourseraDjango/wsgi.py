"""
WSGI config for CourseraDjango project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""
import os
import sys
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CourseraDjango.settings')

path = '/home/tmaus/CourseraDjangoCourse'
if path not in sys.path:
    sys.path.insert(0, path)

application = get_wsgi_application()