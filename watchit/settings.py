"""
Django settings for watchit project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import os
from pathlib import Path
import psycopg2
import psycopg2.extras

con= None
cur = None
try:
    con = psycopg2.connect(
    host="localhost",
    database= "mydb",
    user="postgres",
    password="mypass",
    port="5432"
)

    cur= con.cursor(cursor_factory=psycopg2.extras.DictCursor)

    cur.execute('DROP TABLE IF EXISTS employee')

    create_script= ''' CREATE TABLE IF NOT EXISTS employee(
                            id      int PRIMARY KEY,
                            name    varchar(40) NOT NULL,
                            salary  int,
                            dept_id varchar(30)) '''

    cur.execute(create_script)

    insert_script='INSERT INTO employee(id,name,salary,dept_id) VALUES(%s,%s,%s,%s)'
    insert_values=[(1,'James', 12000, 'D1'),(2,'John', 15000, 'D2'),(3,'Mike', 20000, 'D3'),]
    for record in insert_values:
        cur.execute(insert_script, record)

    update_script ='UPDATE employee SET salary = salary + (salary * 0.5)'
    cur.execute(update_script)

    delete_script='DELETE FROM employee WHERE name = %s'
    delete_record=('James',)
    cur.execute(delete_script, delete_record)

    cur.execute('SELECT * FROM EMPLOYEE')
    for record in cur.fetchall():

        print(record['name'], record['salary'])

    
    con.commit()

    

except Exception as error:
    print(error)
finally:
    if cur is not None:

        cur.close()
    if con is not None: 

        con.close()


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-x=+3p*3!4#uqc39q%vv!d*u23y-v21z7b%-@^0dmzq6hn4x1dy'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

if DEBUG:
    import mimetypes
    mimetypes.add_type('application/javascript','.js', True)

ALLOWED_HOSTS = [
'127.0.0.1',
'backend.michael-soquat.de',
'35.246.161.131'
]

CACHE_TTL= 1
# 60*15

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'videoplatform.apps.VideoplatformConfig',
    "django_rq",
    'debug_toolbar',
    'import_export',
    'user',
    'startscreen',
    'djoser',
    'rest_framework',
    'rest_framework.authtoken',
    'crispy_forms',
    'videos',
    
]

AUTH_USER_MODEL='user.CustomUser'

DJOSER = {
    "USER_ID_FIELD": "username",
    "LOGIN_FIELD": "email",
    "SEND_ACTIVATION_EMAIL": True,
    "ACTIVATION_URL": "activate/{uid}/{token}",
    'SERIALIZERS': {
        'token_create': 'apps.accounts.serializers.CustomTokenCreateSerializer',
    },
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
SITE_NAME = "WATCHIT"

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

RQ_QUEUES = {
    'default': {
        'HOST': 'localhost',
        'PORT': 6379,
        'DB': 0,
        'DEFAULT_TIMEOUT': 360,
    },
}
SECURE_CROSS_ORIGIN_OPENER_POLICY = None
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
    }
}

ROOT_URLCONF = 'watchit.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.static',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'watchit.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'mydb',
#         'USER': 'postgres',
#         'PASSWORD': 'mypass',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True
IMPORT_EXPORT_USE_TRANSACTIONS=True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static/staticfiles",]

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_ROOT= os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

INTERNAL_IPS = [
    "127.0.0.1",
]

