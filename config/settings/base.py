from __future__ import absolute_import, unicode_literals
from pathlib import Path
import environ
import sys
import os

"""
The ocean is older than the mountains,
and is loaded with the memories and dreams of time.
H.P. Lovecraft
"""

ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent.parent
print(ROOT_DIR)

print(ROOT_DIR / ".env")

# dfconfecciones/
APPS_DIR = ROOT_DIR / "blog"
print(APPS_DIR)

env = environ.Env()

READ_DOT_ENV_FILE = env.bool("DJANGO_READ_DOT_ENV_FILE", default=False)
if READ_DOT_ENV_FILE:
    # OS environment variables take precedence over variables from .env
    env.read_env(str(ROOT_DIR / ".env"))

#GENERAL CONFIGURATION----------------------------------------------------------
#DEBUG--------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = env.bool("DJANGO_DEBUG", False)

TIME_ZONE = 'America/La_Paz'

LANGUAGE_CODE = 'es-AR'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True

# https://docs.djangoproject.com/en/dev/ref/settings/#locale-paths
LOCALE_PATHS = [str(ROOT_DIR / "locale")]
#-------------------------------------------------------------------------------

#DATABASE CONFIGURATION--------------------------------------------------------

#Django database por defecto
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': 'mydatabase',
#    }
#}

#Database PostgresSQL suministrada por HEROKU-->gratis, en Add Ons.
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

#Basededatos de PostgresSQL-->creada por mi
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql',
#        'NAME': 'daysiweb',
#        'USER': 'eduardosilva',
#        'PASSWORD': 'Peluchin01',
#        'HOST': 'localhost',
#        'PORT': '5432',
#    }
#}

# ------------------------------------------------------------------------------
ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'

#APP CONFIGURATION--------------------------------------------------------------
DJANGO_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.forms',
]

THIRD_PARTY_APPS = [
    'crispy_forms',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
]

DJANGO_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # "django.contrib.humanize", # Handy template tags
    "django.contrib.admin",
    "django.forms",
]
THIRD_PARTY_APPS = [
    "crispy_forms",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
]

LOCAL_APPS = [
    'blog',
    'photologue',
    'photologue_custom',
    'sortedm2m',
    'contact_form',
    'corsheaders',
    'parler',
    'tinymce',
    'ckeditor',
    'newsletter',
    'easy_thumbnails',
    'phonenumber_field',
    'newsfeed',
]

CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js'

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# MIGRATIONS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#migration-modules
#MIGRATION_MODULES = {"sites": "dfconfecciones.contrib.sites.migrations"}

#-------------------------------------------------------------------------------

#AUTHENTICATION CONFIGURATION---------------------------------------------------
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

AUTH_USER_MODEL = 'blog.User'

LOGIN_REDIRECT_URL = '/'
LOGIN_URL = 'account_login'

AUTOSLUG_SLUGIFY_FUNCTION = 'slugify.slugify'

#-------------------------------------------------------------------------------
# PASSWORDS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#password-hashers
PASSWORD_HASHERS = [
    # https://docs.djangoproject.com/en/dev/topics/auth/passwords/#using-argon2-with-django
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

#-------------------------------------------------------------------------------

#MIDDLEWARE CONFIGURATION-------------------------------------------------------

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.common.BrokenLinkEmailsMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
#-------------------------------------------------------------------------------

#Corsheaders, configuración-----------------------------------------------------
CORS_ALLOWED_ORIGINS = [
    "https://dfconfecciones.herokuapp.com",
    "http://localhost:8080",
    "http://127.0.0.1:9000",
]
#-------------------------------------------------------------------------------

#MEDIA AND STATIC CONFIGURATION------------------------------------------------------


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print(BASE_DIR)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = "/media/"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

#whitenoise#####################################################################
#STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
#STATICFILES_STORAGE = 'dfconfecciones.storage.S3Storage'
#STATIC_HOST = os.environ.get('DJANGO_STATIC_HOST', '')
#STATIC_URL = STATIC_HOST + '/static/'

#-------------------------------------------------------------------------------

#TEMPLATE CONFIGURATION---------------------------------------------------------

TEMPLATES = [
    {
        # https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-TEMPLATES-BACKEND
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
        "DIRS": [str(APPS_DIR / "templates")],
        "OPTIONS": {
            # https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
            # https://docs.djangoproject.com/en/dev/ref/templates/api/#loader-types
            "loaders": [
                "django.template.loaders.filesystem.Loader",
                "django.template.loaders.app_directories.Loader",
            ],
            # https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
                "blog.utils.context_processors.settings_context",
            ],
        },
    }
]

# https://docs.djangoproject.com/en/dev/ref/settings/#form-renderer
FORM_RENDERER = "django.forms.renderers.TemplatesSetting"

CRISPY_TEMPLATE_PACK = 'bootstrap4'

#FIXTURE CONFIGURATION----------------------------------------------------------

FIXTURE_DIRS = (str(APPS_DIR / "fixtures"),)

#-------------------------------------------------------------------------------

# SECURITY
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#session-cookie-httponly
SESSION_COOKIE_HTTPONLY = True
# https://docs.djangoproject.com/en/dev/ref/settings/#csrf-cookie-httponly
CSRF_COOKIE_HTTPONLY = True
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-browser-xss-filter
SECURE_BROWSER_XSS_FILTER = True
# https://docs.djangoproject.com/en/dev/ref/settings/#x-frame-options
X_FRAME_OPTIONS = "DENY"

#-------------------------------------------------------------------------------

#EMAIL CONFIGURATION------------------------------------------------------------
#Mailgun Add On de Heroku
#EMAIL_HOST = os.environ.get('MAILGUN_SMTP_SERVER', '')
#EMAIL_PORT = os.environ.get('MAILGUN_SMTP_PORT', '')
#EMAIL_HOST_USER = os.environ.get('MAILGUN_SMTP_LOGIN', '')
#EMAIL_HOST_PASSWORD = os.environ.get('MAILGUN_SMTP_PASSWORD', '')
#EMAIL_USE_TLS = True

#EMAIL_HOST = env('MAILGUN_SMTP_SERVER', default=None)
#EMAIL_PORT = env('MAILGUN_SMTP_PORT', default=None)
#EMAIL_HOST_USER = env('MAILGUN_SMTP_LOGIN', default=None)
#EMAIL_HOST_PASSWORD = env('MAILGUN_SMTP_PASSWORD', default=None)
#EMAIL_USE_TLS = True

DEFAULT_FROM_EMAIL = env('DJANGO_DEFAULT_FROM_EMAIL',
                         default='PAGINAWEB <paginaweb@dfconfecciones.com>')

SERVER_EMAIL = env('DJANGO_SERVER_EMAIL', default=DEFAULT_FROM_EMAIL)

CONTACT_FORM_RECIPIENTS = (
    ('daysi fernandez', 'dfdtex@gmail.com'),
)

EMAIL_SUBJECT_PREFIX = env('DJANGO_EMAIL_SUBJECT_PREFIX', default='[daysifernandezweb]')

# ADMIN
# ------------------------------------------------------------------------------
ADMIN_URL = "admin/"

ADMINS = [
    ("""Eduardo Silva""", 'dfdtex@hotmail.com'),
]

#MANAGER CONFIGURATION----------------------------------------------------------
MANAGERS = ADMINS

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
        # 'skin': 'office2013',
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
            '/',  # put this to force next toolbar on new line
            {'name': 'yourcustomtools', 'items': [
                # put the name of your editor.ui.addButton here
                'Preview',
                'Maximize',

            ]},
        ],
        'toolbar': 'YourCustomToolbarConfig',  # put selected toolbar config here
        # 'toolbarGroups': [{ 'name': 'document', 'groups': [ 'mode', 'document', 'doctools' ] }],
        # 'height': 291,
        # 'width': '100%',
        # 'filebrowserWindowHeight': 725,
        # 'filebrowserWindowWidth': 940,
        # 'toolbarCanCollapse': True,
        # 'mathJaxLib': '//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML',
        'tabSpaces': 4,
        'extraPlugins': ','.join([
            'uploadimage', # the upload image feature
            # your extra plugins here
            'div',
            'autolink',
            'autoembed',
            'embedsemantic',
            'autogrow',
            # 'devtools',
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

#-------------------------------------------------------------------------------

# django-allauth----------------------------------------------------------------
ACCOUNT_ALLOW_REGISTRATION = env.bool("DJANGO_ACCOUNT_ALLOW_REGISTRATION", True)
# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_AUTHENTICATION_METHOD = "username"
# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_EMAIL_REQUIRED = True
# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_ADAPTER = 'blog.adapters.AccountAdapter'
# https://django-allauth.readthedocs.io/en/latest/configuration.html
SOCIALACCOUNT_ADAPTER = 'blog.adapters.SocialAccountAdapter'

#-------------------------------------------------------------------------------

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

#NEWSLETTER---------------------------------------------------------------------
# Using sorl-thumbnail
NEWSLETTER_THUMBNAIL = 'easy-thumbnails'
# Using django-imperavi
NEWSLETTER_RICHTEXT_WIDGET = "tinymce.widgets.TinyMCE"

# Emails configuration #

# Enabling or Disabling email confirmation
NEWSLETTER_CONFIRM_EMAIL = True

# The delay between each email. Batches en batch size can be specified:
# Amount of seconds to wait between each email. Here 100ms is used.
NEWSLETTER_EMAIL_DELAY = 0.1
# Amount of seconds to wait between each batch. Here one minute is used.
NEWSLETTER_BATCH_DELAY = 60
# Number of emails in one batch
NEWSLETTER_BATCH_SIZE = 100

#Phonenumber Set----------------------------------------------------------------
PHONENUMBER_DB_FORMAT = 'NATIONAL'
PHONENUMBER_DEFAULT_REGION = 'BO'
