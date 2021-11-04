from .base import *

DEBUG = False

ADMINS = (
    ('Iurii K', '31x1962@gmail.com'),
)

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'educa',
        'USER': 'educa',
        'PASSWORD': 'educa',
        'HOST': 'localhost',
    }
}