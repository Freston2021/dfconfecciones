from __future__ import absolute_import, unicode_literals
from boto.s3.connection import OrdinaryCallingFormat
from .base import *
from .base import env

#SECRET CONFIGURATION-----------------------------------------------------------
SECRET_KEY = env('DJANGO_SECRET_KEY')
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


#SECURITY CONFIGURATION---------------------------------------------------------
SECURE_HSTS_SECONDS = 60
SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool(
    'DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS', default=True)
SECURE_HSTS_PRELOAD = True
SECURE_CONTENT_TYPE_NOSNIFF = env.bool(
    'DJANGO_SECURE_CONTENT_TYPE_NOSNIFF', default=True)
SECURE_BROWSER_XSS_FILTER = True
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
SECURE_SSL_REDIRECT = env.bool('DJANGO_SECURE_SSL_REDIRECT', default=True)
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True
X_FRAME_OPTIONS = 'DENY'
SECURE_REFERRER_POLICY = 'strict-origin'


#STORAGE CONFIGURATION----------------------------------------------------------
INSTALLED_APPS += ['gunicorn', ]

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

#EMAIL--------------------------------------------------------------------------

#Anymail with Mailgun
INSTALLED_APPS += ['anymail', ]
ANYMAIL = {
    'MAILGUN_API_KEY': 'key-48650e6634bd972b621fae537f39cafa',
    'MAILGUN_SENDER_DOMAIN': 'sandboxd3d8ace8e76c47dcb7a7507df5c56455.mailgun.org'
}
#EMAIL_BACKEND = 'anymail.backends.mailgun.EmailBackend'

#-------------------------------------------------------------------------------

#Email Backend de Django
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

#-------------------------------------------------------------------------------

#Varios Email Sender:
#MAilgun-------------------
EMAIL_HOST = os.environ.get('MAILGUN_SMTP_SERVER', '')
EMAIL_PORT = os.environ.get('MAILGUN_SMTP_PORT', '')
EMAIL_HOST_USER = os.environ.get('MAILGUN_SMTP_LOGIN', '')
EMAIL_HOST_PASSWORD = os.environ.get('MAILGUN_SMTP_PASSWORD', '')
#-----------------------------------------------------------------

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

#TEMPLATE CONFIGURATION---------------------------------------------------------
TEMPLATES[0]['OPTIONS']['loaders'] = [
    ('django.template.loaders.cached.Loader', [
        'django.template.loaders.filesystem.Loader', 'django.template.loaders.app_directories.Loader', ]),
]


#DATABASE CONFIGURATION---------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dfihb1lvp6qp9k',
        'USER': 'btvocdbcaidbla',
        'PASSWORD': 'b9c8d202ddf236ddc72f314cb9ddd6388e9a96ce6838ff9e6a2e2627aca6f919',
        'HOST': 'ec2-3-215-83-124.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

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

#CACHING------------------------------------------------------------------------
REDIS_LOCATION = '{0}/{1}'.format(env('REDIS_URL', default='redis://127.0.0.1:6379'), 0)

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': REDIS_LOCATION,
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'IGNORE_EXCEPTIONS': True,
        }
    }
}


#LOGGING CONFIGURATION----------------------------------------------------------
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s '
                      '%(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false', ],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins', ],
            'level': 'ERROR',
            'propagate': True
        },
        'django.security.DisallowedHost': {
            'level': 'ERROR',
            'handlers': ['console', 'mail_admins', ],
            'propagate': True
        }
    }
}
