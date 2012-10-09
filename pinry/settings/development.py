from pinry.settings import *

import os


DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(SITE_ROOT, 'development.db'),
    }
}

SECRET_KEY = 'ZDQyMDBjZDYtYjVlZS00ZGEzLWJlMzktMWVhM2Q0NDM4OWIz'

# facebook config
FACEBOOK_APP_ID = '434190746638873'
FACEBOOK_API_SECRET = '7301d5cd2d4d29ae0474b762490ab42c'
FACEBOOK_EXTENDED_PERMISSIONS = ['publish_stream']

# twitter config
TWITTER_CONSUMER_KEY = 'j9QEx1MjA9nOi2rlS5fFg'
TWITTER_CONSUMER_SECRET = 'irBDnv1HM0eHxxcVJUJG53g42s8qRFs9yA1VUjVRcRM'
