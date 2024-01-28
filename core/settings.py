# -*- encoding: utf-8 -*-


import os

from decouple import config
from unipath import Path

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__).parent
CORE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY', default='S#perS3crEt_1122')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True, cast=bool)

# load production server from .env
ALLOWED_HOSTS        = ["*"]
CSRF_TRUSTED_ORIGINS = ['http://localhost:85', 'http://127.0.0.1', 'https://' + config('SERVER', default='127.0.0.1')]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
CRISPY_TEMPLATE_PACK = 'bootstrap4'
AUTH_USER_MODEL = 'authentication.User'

# Application definition
INSTALLED_APPS = [
    'menu',
    'calculation',
    'django_tables2',
    'django_filters',
    'apps.home',
    'apps.authentication',
    'apps.farming',
    'apps.finance',
    'apps.inventory',
    'apps.supplies',
    'apps.sales',
    'apps.reports',
    'apps.documentation',
    'crispy_forms',
    'extra_views',
    'dal',
    'dal_select2',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'
LOGIN_REDIRECT_URL = "login"  # Route defined in home/urls.py
LOGOUT_REDIRECT_URL = "login"  # Route defined in home/urls.py
TEMPLATE_DIR = os.path.join(CORE_DIR, "apps/templates")  # ROOT dir for templates

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'core.context_processors.empresa'
            ],
            'libraries':{
                'formset_tags': 'core.templatetags.formset_tags',
            }
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'turbo_potato',
#         'USER': '',
#         'PASSWORD': '',
#         'HOST': 'localhost',
#         'PORT': '3306',
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'es-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True



#############################################################
# SRC: https://devcenter.heroku.com/articles/django-assets

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(CORE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(CORE_DIR, 'apps/static'),
)

EXPORT_PDF_CSS = {
    "portrait":os.path.join(STATICFILES_DIRS[0],"assets/css/export_pdf/portrait.css"),
    "landscape":os.path.join(STATICFILES_DIRS[0],"assets/css/export_pdf/landscape.css"),
    "invoice_css":os.path.join(STATICFILES_DIRS[0],"assets/css/export_pdf/invoice.css"),
    "invoice_img":os.path.join(STATICFILES_DIRS[0],"assets/img/logo.png"),
}

DOCUMENTATION_ROOT = os.path.join(BASE_DIR, 'docs')
DOCUMENTATION_HTML_ROOT = os.path.join(CORE_DIR, 'site')
DOCUMENTATION_ACCESS_FUNCTION = lambda user: user.is_active

print(DOCUMENTATION_HTML_ROOT)

# Django-mkdocs assumes an Nginx server is used by default to serve the documentation. 
# DOCUMENTATION_XSENDFILE is set to true by default. If you are not using Nginx, expect
# a very small number of users, and understand the consequences of using django.views.static.serve,
# set the following flag to False:
DOCUMENTATION_XSENDFILE = False

EMPRESA = {
    "nombre":"Agro Atardecer",
    "razon_social":"Agro Atardecer S.A",
    "ruc":"80049687-6",
    "rubro":"PRODUCCION AGRICOLA Y VENTA DE INSUMOS",
    "telefono":"0971 436141",
    "fax":"0528 222123",
    "pais":"PARAGUAY",
    "departamento":"CAAGUAZU",
    "localidad":"SAN MIGUEL",
    "direccion":"RUTA PY13 - KM 40,5",
    "timbrado":{
        "numero":"12332145",
        "fecha_inicio":"01/01/2022",
        "fecha_fin":"31/12/2022",
        "autorizacion":"350050010670"
    }
}

#############################################################
#############################################################
