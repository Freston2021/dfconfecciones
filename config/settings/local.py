import socket
import os
from .base import *


#DEBUG--------------------------------------------------------------------------
DEBUG = env.bool('DJANGO_DEBUG', default=True)
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG


#SECRET CONFIGURATION-----------------------------------------------------------
SECRET_KEY = env('DJANGO_SECRET_KEY', default='%,%2`oTuz!5Dp~-3}3{kb3r;N`oZ+9xOUCwDI.p!TP:*48H#B$')


#MAIL SETTINGS------------------------------------------------------------------
EMAIL_PORT = 1025
EMAIL_HOST = 'smtp.mailgun.org'
EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND',
                   default='django.core.mail.backends.console.EmailBackend')


#CACHING------------------------------------------------------------------------
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': ''
    }
}


#DJANGO-DEBUG-TOOLBAR-----------------------------------------------------------
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]
INSTALLED_APPS += ['debug_toolbar']

INTERNAL_IPS = ['127.0.0.1', '10.0.2.2', ]

# tricks to have debug toolbar when developing with docker
if os.environ.get('USE_DOCKER') == 'yes':
    ip = socket.gethostbyname(socket.gethostname())
    INTERNAL_IPS += [ip[:-1] + '1']

ALLOWED_HOSTS = ['127.0.0.1']

DEBUG_TOOLBAR_CONFIG = {
    'DISABLE_PANELS': [
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ],
    'SHOW_TEMPLATE_CONTEXT': True,
}


#DJANGO-EXTENSIONS--------------------------------------------------------------
INSTALLED_APPS += ['django_extensions']


#TESTING------------------------------------------------------------------------
TEST_RUNNER = 'django.test.runner.DiscoverRunner'