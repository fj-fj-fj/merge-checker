import os

from .base import BASE_DIR

SECRET_KEY = os.environ.get(
    'SECRET_KEY',
    '# This string is enough for testing :)'  # FIXME
)

DEBUG = True  # FIXME False

ADMIN = os.environ.get('ADMIN')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    'optional': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': '5432',
    },
}
