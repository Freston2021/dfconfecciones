from __future__ import absolute_import, unicode_literals
from boto.s3.connection import OrdinaryCallingFormat
from .base import *
from .base import env

# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = env("DJANGO_SECRET_KEY")
# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=["dfconfecciones.herokuapp.com"])

#CACHING------------------------------------------------------------------------
#REDIS_LOCATION = '{0}/{1}'.format(env('REDIS_URL', default='redis://127.0.0.1:6379'), 0)
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': env("REDIS_URL"),
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'IGNORE_EXCEPTIONS': True,
        }
    }
}

# SECURITY
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-proxy-ssl-header
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-ssl-redirect
SECURE_SSL_REDIRECT = env.bool("DJANGO_SECURE_SSL_REDIRECT", default=True)
# https://docs.djangoproject.com/en/dev/ref/settings/#session-cookie-secure
SESSION_COOKIE_SECURE = True
# https://docs.djangoproject.com/en/dev/ref/settings/#csrf-cookie-secure
CSRF_COOKIE_SECURE = True
# https://docs.djangoproject.com/en/dev/topics/security/#ssl-https
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-hsts-seconds
# TODO: set this to 60 seconds first and then to 518400 once you prove the former works
SECURE_HSTS_SECONDS = 60
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-hsts-include-subdomains
SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool(
    "DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS", default=True
)
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-hsts-preload
SECURE_HSTS_PRELOAD = env.bool("DJANGO_SECURE_HSTS_PRELOAD", default=True)
# https://docs.djangoproject.com/en/dev/ref/middleware/#x-content-type-options-nosniff
SECURE_CONTENT_TYPE_NOSNIFF = env.bool(
    "DJANGO_SECURE_CONTENT_TYPE_NOSNIFF", default=True
)

#gunicorn???????----------------------------------------------------------------
INSTALLED_APPS += ['gunicorn', ]
#-------------------------------------------------------------------------------

#STORAGE CONFIGURATION----------------------------------------------------------

#Usando el mismo que Local, esta la configuración en Base.py--Media y Static----
#-------------------------------------------------------------------------------

#AWS S3----OJO!!!! es gratis hasta cierto limite!!!-----------------------

#AWS_ACCESS_KEY_ID = env("DJANGO_AWS_ACCESS_KEY_ID")
#AWS_SECRET_ACCESS_KEY = env("DJANGO_AWS_SECRET_ACCESS_KEY")
#AWS_STORAGE_BUCKET_NAME = env("DJANGO_AWS_STORAGE_BUCKET_NAME")
#AWS_QUERYSTRING_AUTH = False
#_AWS_EXPIRY = 60 * 60 * 24 * 7
#AWS_S3_OBJECT_PARAMETERS = {
#    "CacheControl": f"max-age={_AWS_EXPIRY}, s-maxage={_AWS_EXPIRY}, must-revalidate"
#}
#AWS_S3_REGION_NAME = env("DJANGO_AWS_S3_REGION_NAME", default=None)
#AWS_S3_CUSTOM_DOMAIN = env("DJANGO_AWS_S3_CUSTOM_DOMAIN", default=None)
#aws_s3_domain = AWS_S3_CUSTOM_DOMAIN or f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"

#MEDIA_URL = 'https://s3.amazonaws.com/%s/' % AWS_STORAGE_BUCKET_NAME
#STATIC_URL = 'https://s3.amazonaws.com/%s/' % AWS_STORAGE_BUCKET_NAME

#DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
#-------------------------------------------------------------------------------

# TEMPLATES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES[-1]["OPTIONS"]["loaders"] = [  # type: ignore[index] # noqa F405
    (
        "django.template.loaders.cached.Loader",
        [
            "django.template.loaders.filesystem.Loader",
            "django.template.loaders.app_directories.Loader",
        ],
    )
]

#EMAIL--------------------------------------------------------------------------

#Anymail with Mailgun(cuenta dfdtex@gmail.com)
#INSTALLED_APPS += ['anymail', ]
#ANYMAIL = {
#    'MAILGUN_API_KEY': 'key-48650e6634bd972b621fae537f39cafa',
#    'MAILGUN_SENDER_DOMAIN': 'sandboxd3d8ace8e76c47dcb7a7507df5c56455.mailgun.org'
#}
#EMAIL_BACKEND = 'anymail.backends.mailgun.EmailBackend'

#-------------------------------------------------------------------------------

#Email Backend de Django
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

#-------------------------------------------------------------------------------

#Varios Email Sender:-----------------------------------------------------------

#MAilgun add on de Heroku configurado en Base.py
#Plan-->Free-------------------Prueba----------

#3 correos autorizados(Authorized Recipients):
                        #dfdtex@gmail.com;
                        #epoealan@gmail.com;
                        #silvaeduardojavier@hotmail.com
#-------------------------------------------------------------------------------

#SendGrid---------------------
#SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')
#EMAIL_HOST = 'smtp.sendgrid.net'
#EMAIL_HOST_USER = 'apikey' # this is exactly the value 'apikey'
#EMAIL_HOST_PASSWORD = SENDGRID_API_KEY
#EMAIL_PORT = 587
#EMAIL_USE_TLS = True

#Gmail------------------------
#EMAIL_HOST = 'smtp.gmail.com'
#EMAIL_HOST_USER = env('DJANGO_USER_MAIL')
#EMAIL_HOST_PASSWORD = env('DJANGO_USER_MAIL_PASSWORD')
#EMAIL_PORT = 587
#EMAIL_USE_TLS = True

#Mailjet----------------------
#MAILJET_API_KEY = os.getenv('MAILJET_API_KEY')
#EMAIL_HOST = 'in-v3.mailjet.com'
#EMAIL_HOST_USER = '892b5344ed2f16c4368835b6650b5067'
#EMAIL_HOST_PASSWORD = MAILJET_API_KEY
#EMAIL_PORT = 587
#EMAIL_USE_TLS = True
#-------------------------------------------------------------------------------

#DATABASE CONFIGURATION---------------------------------------------------------

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql',
#        'NAME': 'd6e8em33ojgbu4',
#        'USER': 'nadkhlhuxgequn',
#        'PASSWORD': 'a1a13d16b56c95fab760d8fdc4ba723ed74ccddaf9808b58cabf43a3509aea4f',
#        'HOST': 'ec2-18-214-214-252.compute-1.amazonaws.com',
#        'PORT': '5432',
#    }
#}

# Collectfast
# ------------------------------------------------------------------------------
# https://github.com/antonagestam/collectfast#installation
INSTALLED_APPS = ["collectfast"] + INSTALLED_APPS  # noqa F405


#LOGGING CONFIGURATION----------------------------------------------------------
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {"require_debug_false": {"()": "django.utils.log.RequireDebugFalse"}},
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s "
            "%(process)d %(thread)d %(message)s"
        }
    },
    "handlers": {
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler",
        },
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "root": {"level": "INFO", "handlers": ["console"]},
    "loggers": {
        "django.request": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": True,
        },
        "django.security.DisallowedHost": {
            "level": "ERROR",
            "handlers": ["console", "mail_admins"],
            "propagate": True,
        },
    },
}

#newsfeed configuration---------------------------------------------------------
NEWSFEED_SITE_BASE_URL = 'https://dfconfecciones.herokuapp.com'
