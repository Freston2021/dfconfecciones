from __future__ import absolute_import, unicode_literals

import environ
import sys
import os
import django_heroku

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = environ.Path(__file__) - 3
APPS_DIR = ROOT_DIR.path('blog')

env = environ.Env()

READ_DOT_ENV_FILE = env.bool('DJANGO_READ_DOT_ENV_FILE', default=False)

if READ_DOT_ENV_FILE:
    env_file = str(ROOT_DIR.path('.env'))
    print('Loading : {}'.format(env_file))
    env.read_env(env_file)
    print('The .env file has been loaded. See base.py for more information')


#APP CONFIGURATION--------------------------------------------------------------
DJANGO_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
]

THIRD_PARTY_APPS = [
    'crispy_forms',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
]

LOCAL_APPS = [
    'blog',
    'photologue',
    'photologue_custom',
    'sortedm2m',
    'contact_form',
    'ckeditor',
    'corsheaders',
    'parler',
]

CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js'

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


#SITE CONFIGURATION-------------------------------------------------------------
ALLOWED_HOSTS = ['0.0.0.0', 'localhost', '127.0.0.1', 'dfconfecciones.herokuapp.com']

CORS_ALLOWED_ORIGINS = [
    "https://dfconfecciones.herokuapp.com",
    "http://localhost:8080",
    "http://127.0.0.1:9000",
]

#MIDDLEWARE CONFIGURATION-------------------------------------------------------
MIDDLEWARE_CLASSES = (
    # Simplified static file serving.
    # https://warehouse.python.org/project/whitenoise/
    'whitenoise.middleware.WhiteNoiseMiddleware',)

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]




#DEBUG--------------------------------------------------------------------------
#DEBUG = False
# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = env.bool("DJANGO_DEBUG", False)


#FIXTURE CONFIGURATION----------------------------------------------------------
FIXTURE_DIRS = (
    str(APPS_DIR.path('fixtures')),
)


#EMAIL CONFIGURATION------------------------------------------------------------
CONTACT_FORM_RECIPIENTS = (
    ('daysi fernandez', 'dfdtex@gmail.com'),
)


#MANAGER CONFIGURATION----------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = [
    ("""Eduardo Silva""", 'dfdtex@hotmail.com'),
]

MANAGERS = ADMINS


#DATABASE CONFIGURATION--------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'daysiweb',
        'USER': 'eduardosilva',
        'PASSWORD': 'Peluchin01',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}


#GENERAL CONFIGURATION----------------------------------------------------------
TIME_ZONE = 'America/La_Paz'

LANGUAGE_CODE = 'es-AR'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True

#TEMPLATE CONFIGURATION---------------------------------------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            str(APPS_DIR.path('templates')),
        ],
        'OPTIONS': {
            'debug': DEBUG,
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'


#STATIC FILE CONFIGURATION------------------------------------------------------
#BASE_DIR devuelve la ruta base de la app
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#print ("base dir path -->", BASE_DIR)

#MEDIA_ROOT es la carpeta donde irán los archivos cargados usando FileField.
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")
#print ("Media Root path -->", MEDIA_ROOT)

MEDIA_URL = '/media/'
#print ("Media Url path -->", MEDIA_URL)

#STATIC_ROOT es la carpeta donde se almacenarán los archivos estáticos,
#después de usar manage.py collectstatic.
#STATIC_ROOT solo se requiere para la implementación, mientras esta en
#desarrollo, Django busca archivos estáticos dentro del directorio de cada aplicación.
#Esta es la magia realizada por manage.py runserver cuando DEBUG=True.
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
#print ("Static Root path -->", STATIC_ROOT)

#STATIC_URL = '/static/'
#print ("Static Url path -->", STATIC_URL)

#STATICFILES_DIRS es la lista de carpetas donde Django buscará archivos estáticos
#adicionales además de la carpeta static de cada aplicación instalada.
#Esta configuración define las ubicaciones adicionales que atravesará la aplicación
#staticfiles si el FileSystemFinder Finder está habilitado, p. si usa el comando de
#administración collectstatic o findstatic o usa la vista de publicación de
#archivos estáticos.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'staticfiles'),
)
#print ("Staticfiles Dirs path -->", STATICFILES_DIRS)

#whitenoise#####################################################################
STATIC_HOST = os.environ.get('DJANGO_STATIC_HOST', '')
STATIC_URL = STATIC_HOST + '/static/'


# ------------------------------------------------------------------------------
ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'


#PASSWORD VALIDATION------------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


#AUTHENTICATION CONFIGURATION---------------------------------------------------
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

ACCOUNT_AUTHENTICATION_METHOD = 'username'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

ACCOUNT_ALLOW_REGISTRATION = env.bool('DJANGO_ACCOUNT_ALLOW_REGISTRATION', True)
ACCOUNT_ADAPTER = 'blog.adapters.AccountAdapter'
SOCIALACCOUNT_ADAPTER = 'blog.adapters.SocialAccountAdapter'

AUTH_USER_MODEL = 'blog.User'

LOGIN_REDIRECT_URL = '/'
LOGIN_URL = 'account_login'

AUTOSLUG_SLUGIFY_FUNCTION = 'slugify.slugify'

ADMIN_URL = r'^admin/'


#LOGGING CONFIGURATION----------------------------------------------------------

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    # Formatting of messages.
    'formatters': {
        # Don't need to show the time when logging to console.
        'console': {
            'format': '%(levelname)s %(name)s.%(funcName)s (%(lineno)d) %(message)s'
        }
    },
    # The handlers decide what we should do with a logging message - do we email
    # it, ditch it, or write it to a file?
    'handlers': {
        # Writing to console. Use only in dev.
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'console'
        },
        # Send logs to /dev/null.
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
    },

    # Loggers decide what is logged.
    'loggers': {
        '': {
            # Default (suitable for dev) is to log to console.
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        'photologue': {
            # Default (suitable for dev) is to log to console.
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        # logging of SQL statements. Default is to ditch them (send them to
        # null). Note that this logger only works if DEBUG = True.
        'django.db.backends': {
            'handlers': ['null'],
            'level': 'DEBUG',
            'propagate': False,
        },
    }
}


# Don't display logging messages to console during unit test runs.
if len(sys.argv) > 1 and sys.argv[1] == 'test':
    LOGGING['loggers']['']['handlers'] = ['null']
    LOGGING['loggers']['photologue']['handlers'] = ['null']


#CKEDITOR_CONFIGS---------------------------------------------------------------
CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'kama',
        'toolbar_Basic': [
            ['Source', '-', 'Bold', 'Italic']
        ],
        'toolbar_YourCustomToolbarConfig': [
            {'name': 'document', 'items': ['Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates']},
            {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
            {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll']},
            {'name': 'forms',
             'items': ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton',
                       'HiddenField']},
            '/',
            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
                       'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl',
                       'Language']},
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            {'name': 'insert',
             'items': ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe']},
            '/',
            {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
            {'name': 'about', 'items': ['About']},
            '/',
            {'name': 'yourcustomtools', 'items': [
                'Preview',
                'Maximize',

            ]},
        ],
        'toolbar': 'YourCustomToolbarConfig',
        'tabSpaces': 4,
        'extraPlugins': ','.join(
            [
                'div',
                'autolink',
                'autoembed',
                'embedsemantic',
                'autogrow',
                'widget',
                'lineutils',
                'clipboard',
                'dialog',
                'dialogui',
                'elementspath'
            ]),
    }
}

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

#SENTRY_SDK---------------------------------------------------------------------
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="https://examplePublicKey@o0.ingest.sentry.io/0",
    integrations=[DjangoIntegration()],

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)

# Activate Django-Heroku.
django_heroku.base(locals())
