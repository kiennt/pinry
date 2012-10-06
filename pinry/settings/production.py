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
FB_APP_ID = '125531010927495'
FB_APP_SECRET = '5ea4053396fbca1eb36d850f8a2819cb'

# twitter config
TWITTER_CONSUMER_KEY = ''
TWITTER_CONSUMER_SECRET = ''
