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


#STATIC FILE CONFIGURATION------------------------------------------------------
#BASE_DIR devuelve la ruta base de la app
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#print ("base dir path -->", BASE_DIR)

#MEDIA_ROOT es la carpeta donde irán los archivos cargados usando FileField.
#MEDIA_ROOT = os.path.join(BASE_DIR, "media/")
MEDIA_ROOT = os.path.join(BASE_DIR, "live-static", "media-root")

#print ("Media Root path -->", MEDIA_ROOT)

MEDIA_URL = '/media/'
#print ("Media Url path -->", MEDIA_URL)

#STATIC_ROOT es la carpeta donde se almacenarán los archivos estáticos,
#después de usar manage.py collectstatic.
#STATIC_ROOT solo se requiere para la implementación, mientras esta en
#desarrollo, Django busca archivos estáticos dentro del directorio de cada aplicación.
#Esta es la magia realizada por manage.py runserver cuando DEBUG=True.
#STATIC_ROOT = os.path.join(BASE_DIR, "static/")
STATIC_ROOT = os.path.join(BASE_DIR, "live-static", "static-root")

#print ("Static Root path -->", STATIC_ROOT)

STATIC_URL = '/static/'
#print ("Static Url path -->", STATIC_URL)

#STATICFILES_DIRS es la lista de carpetas donde Django buscará archivos estáticos
#adicionales además de la carpeta static de cada aplicación instalada.
#Esta configuración define las ubicaciones adicionales que atravesará la aplicación
#staticfiles si el FileSystemFinder Finder está habilitado, p. si usa el comando de
#administración collectstatic o findstatic o usa la vista de publicación de
#archivos estáticos.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
#print ("Staticfiles Dirs path -->", STATICFILES_DIRS)



#TESTING------------------------------------------------------------------------
TEST_RUNNER = 'django.test.runner.DiscoverRunner'
