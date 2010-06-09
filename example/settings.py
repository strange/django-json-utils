import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG
DEBUG_PROPAGATE_EXCEPTIONS = DEBUG
 
DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = ':memory:'

TIME_ZONE = 'UTC'
    
SITE_ID = 1
      
SECRET_KEY = '00000000000000000000000000000000000000000000000000'

ROOT_URLCONF = 'example.urls'

TEMPLATE_DIRS = (
    os.path.join(os.path.abspath(os.path.dirname(__file__)), 'templates')
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'json_utils',
    'example.stuff',
)
