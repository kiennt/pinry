from pinry.settings import *

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

SECRET_KEY = 'NTQ3ZjBhMDMtNmE1ZC00MDU5LWJmNjUtMzNkNmY1NjgwYjZl'

# facebook config
FACEBOOK_APP_ID = '125531010927495'
FACEBOOK_API_SECRET = '2300048e60f81cc1416572f796bcfdb1'
FACEBOOK_EXTENDED_PERMISSIONS = ['publish_stream']

# twitter config
TWITTER_CONSUMER_KEY = 'IS0PKMs1syZLkMdQ9JbDLw'
TWITTER_CONSUMER_SECRET = 'OPMmryLWgk34fOhMO6Pgdel9G6I6GZfXIeygX2NA6a4'
