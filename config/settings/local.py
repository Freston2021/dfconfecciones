import socket
import os
from .base import *
from .base import env

#DEBUG--------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True

#TEMPLATES[0]['OPTIONS']['debug'] = DEBUG


#SECRET CONFIGURATION-----------------------------------------------------------
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="zy0UD54lKRbeZnfjnTFjYivOV8zUfusqTPtDFRmD2uM1Debpc0Unjy4Rc4sbhTg0",
)

# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]

#MAIL SETTINGS------------------------------------------------------------------
#EMAIL_PORT = 1025
#EMAIL_HOST = 'smtp.mailgun.org'
#EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND',
#                   default='django.core.mail.backends.console.EmailBackend')

#EMAIL_HOST = 'smtp.gmail.com'
#EMAIL_HOST_USER = env('DJANGO_USER_MAIL')
#EMAIL_HOST_PASSWORD = env('DJANGO_USER_MAIL_PASSWORD')
#EMAIL_PORT = 587
#EMAIL_USE_TLS = True

#-------------------------------------------------------------------------------
#MAilgun de la cuenta dfdtex@gmail.com, autorizando contactos que reciben-------

#MAILGUN_PASSWORD_KEY = os.getenv('MAILGUN_PASSWORD_KEY')
#EMAIL_HOST = 'smtp.mailgun.org'
#EMAIL_HOST_USER = 'postmaster@sandboxd3d8ace8e76c47dcb7a7507df5c56455.mailgun.org'
#EMAIL_HOST_PASSWORD = MAILGUN_PASSWORD_KEY
#EMAIL_PORT = 587
#EMAIL_USE_TLS = True


#CACHING------------------------------------------------------------------------
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': ''
    }
}

#DJANGO-DEBUG-TOOLBAR-----------------------------------------------------------
INSTALLED_APPS += ['debug_toolbar', ]

MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware",]

DEBUG_TOOLBAR_CONFIG = {
    "DISABLE_PANELS": ["debug_toolbar.panels.redirects.RedirectsPanel"],
    "SHOW_TEMPLATE_CONTEXT": True,
}

INTERNAL_IPS = ["127.0.0.1", "10.0.2.2"]
#if env("USE_DOCKER") == "yes":
#    import socket
#
#    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
#    INTERNAL_IPS += [".".join(ip.split(".")[:-1] + ["1"]) for ip in ips]
#    try:
#        _, _, ips = socket.gethostbyname_ex("node")
#        INTERNAL_IPS.extend(ips)
#    except socket.gaierror:
        # The node container isn't started (yet?)
#        pass

#DJANGO-EXTENSIONS--------------------------------------------------------------
INSTALLED_APPS += ['django_extensions']


#TESTING------------------------------------------------------------------------
TEST_RUNNER = 'django.test.runner.DiscoverRunner'
