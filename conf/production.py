from common import *

DEBUG=False
#Start up logging to the console

#FILE_HANDLER = logging.FileHandler(os.path.join(PROJECT_ROOT)+'/django.log', 'w')
FILE_HANDLER = logging.FileHandler('/var/www/vhosts/twy_production/logs/django.log', 'w')
logging.getLogger('').addHandler(FILE_HANDLER)
logging.info("Django Started")

CACHE_BACKEND = 'memcached://127.0.0.1:11211/'
CACHE_MIDDLEWARE_SECONDS = 10

DATABASES = {
    'default': {
        'NAME':'twyck',
        'ENGINE':'django.db.backends.postgresql_psycopg2',
        'USER':'twyck',
        'PASSWORD':'timberwyckfarm1',
    },
}

MEDIA_ROOT=os.path.join(PROJECT_ROOT, 'media/')
MEDIA_URL = 'http://www.timberwyckfarm.com/media/'
STATIC_URL = '/media/'
ADMIN_MEDIA_PREFIX=MEDIA_URL+'admin/'

TEMPLATE_DIRS = (os.path.join(PROJECT_ROOT, 'templates'),)

INTERNAL_IPS = ()

##### For Email ########
ACCOUNT_ACTIVATION_DAYS=15
EMAIL_HOST="smtp.gmail.com"
EMAIL_HOST_USER="colin.powell@gmail.com"
EMAIL_HOST_PASSWORD="hall6-jerkin"
DEFAULT_FROM_EMAIL="info@timberwyckfarm.com"
EMAIL_USE_TLS = True
