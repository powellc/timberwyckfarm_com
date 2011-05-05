from common import *

DEBUG=True
TESTING=False
TEMPLATE_DEBUG = DEBUG

import os
if os.path.exists('/home/powellc'):
	dev_db = '/home/powellc/projects/timberwyckfarm/build/timberwyckfarm_com/dev.sqlite3'
else:
	dev_db = '/Users/powellc/projects/timberwyckfarm/build/timberwyckfarm_com/dev.sqlite3'

if DEBUG:
    DATABASES = {
        'default': {
            'NAME': PROJECT_ROOT+'/dev.sqlite3',
            'ENGINE': 'django.db.backends.sqlite3',
        },
    }
    MEDIA_URL='http://127.0.0.1:8000/media/'
    MEDIA_ROOT= os.path.join(PROJECT_ROOT, 'media/')

ADMIN_MEDIA_PREFIX=MEDIA_URL+'admin/'

TEMPLATE_DIRS = (os.path.join(PROJECT_ROOT, 'templates'),)

ACCOUNT_ACTIVATION_DAYS = 7

INTERNAL_IPS = ('24.93.128.34','10.1.1.23','127.0.0.1' )
VIRTUALENV="/home/powellc/.virtualenvs/twyck/lib/python2.5/site-packages"

#Start up logging to the console

logging.getLogger('').addHandler(CONSOLE_HANDLER)
logging.debug("Django Started")

RECAPTCHA_PUBLIC_KEY = ''
RECAPTCHA_PRIVATE_KEY = ''

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

##### For Email ########
ACCOUNT_ACTIVATION_DAYS=15
EMAIL_HOST="mail.onecardinal.com"
EMAIL_HOST_USER="colin@onecardinal.com"
EMAIL_HOST_PASSWORD="hall6-jerkin"
DEFAULT_FROM_EMAIL="info@onecardinal.com"
EMAIL_USE_TLS = True

CACHE_DIR = os.path.join(SITE_ROOT, 'var',  'cache/')
CACHE_BACKEND = 'file:///' + CACHE_DIR
CACHE_TIMEOUT = 60*5

