from pinry.settings import *

import os


DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dcfpu5b0n124ds',
        'HOST': 'ec2-107-22-170-43.compute-1.amazonaws.com',
        'PORT': 5432,
        'USER': 'alxuptovzlebxz',
        'PASSWORD': 'PkmnKvBpoqwYhk4gZcbXCMsGGr'
    }
}

SECRET_KEY = '74ee58e8-0c43-11e2-b3c8-406c8f3d3467'
