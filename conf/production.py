from common import *

DEBUG=False
#Start up logging to the console

logging.getLogger('').addHandler(FILE_HANDLER)
logging.getLogger('keyedcache').setLevel(logging.INFO)
logging.info("Django Started")

CACHE_BACKEND = 'memcached://127.0.0.1:11211/'
CACHE_MIDDLEWARE_SECONDS = 10

DATABASE_HOST='bradbury'
DATABASE_ENGINE = 'postgresql_psycopg2'
DATABASE_NAME = 'pbp'
DATABASE_USER = 'pbp'
DATABASE_PASSWORD = 'P3Prnwb'

MEDIA_ROOT=os.path.join(PROJECT_ROOT, 'media/')
MEDIA_URL = 'http://penobscotbaypress.com/media/'
ADMIN_MEDIA_PREFIX=MEDIA_URL+'admin/'

TEMPLATE_DIRS = (os.path.join(PROJECT_ROOT, 'templates'),)

INTERNAL_IPS = ('192.168.2.2', '192.168.0.153','24.93.128.34','10.1.1.23','127.0.0.1','67.251.7.81' )

#API key is for penobscotbaypress.com
GOOGLE_API_KEY='ABQIAAAATux_aKmAEX7DnojAr8SqlRTyl9CS5q3L9FIn7JSvfaKvyESzUhR20N-9Pqstiw45F-wXH6msAoVaKw'

##### For Email ########
ACCOUNT_ACTIVATION_DAYS=15
EMAIL_HOST="smtp.3ip.net"
EMAIL_HOST_USER="cpowell@penobscotbaypress.com"
EMAIL_HOST_PASSWORD="cpow07"
DEFAULT_FROM_EMAIL="cpowell@penobscotbaypress.com"
EMAIL_USE_TLS = True
