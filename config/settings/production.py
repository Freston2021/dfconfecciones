from __future__ import absolute_import, unicode_literals
from boto.s3.connection import OrdinaryCallingFormat
#from django.utils import six
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
INSTALLED_APPS += ['gunicorn', 'storages', ]
#INSTALLED_APPS += ['gunicorn',]

AWS_ACCESS_KEY_ID = env("DJANGO_AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = env("DJANGO_AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = env("DJANGO_AWS_STORAGE_BUCKET_NAME")
AWS_QUERYSTRING_AUTH = False
_AWS_EXPIRY = 60 * 60 * 24 * 7
AWS_S3_OBJECT_PARAMETERS = {
    "CacheControl": f"max-age={_AWS_EXPIRY}, s-maxage={_AWS_EXPIRY}, must-revalidate"
}
AWS_S3_REGION_NAME = env("DJANGO_AWS_S3_REGION_NAME", default=None)
AWS_S3_CUSTOM_DOMAIN = env("DJANGO_AWS_S3_CUSTOM_DOMAIN", default=None)
aws_s3_domain = AWS_S3_CUSTOM_DOMAIN or f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"

MEDIA_URL = 'https://s3.amazonaws.com/%s/' % AWS_STORAGE_BUCKET_NAME

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
#STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
#EMAIL--------------------------------------------------------------------------
DEFAULT_FROM_EMAIL = env('DJANGO_DEFAULT_FROM_EMAIL',
                         default='PAGINAWEB <paginaweb@daysifernandez.com>')

EMAIL_SUBJECT_PREFIX = env('DJANGO_EMAIL_SUBJECT_PREFIX', default='[daysiweb]')

SERVER_EMAIL = env('DJANGO_SERVER_EMAIL', default=DEFAULT_FROM_EMAIL)

# Anymail with Mailgun
INSTALLED_APPS += ['anymail', ]

ANYMAIL = {
    'MAILGUN_API_KEY': 'key-48650e6634bd972b621fae537f39cafa',
    'MAILGUN_SENDER_DOMAIN': 'sandboxd3d8ace8e76c47dcb7a7507df5c56455.mailgun.org'
}
EMAIL_BACKEND = 'anymail.backends.mailgun.EmailBackend'


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
