DEBUG=True

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

ALLOWED_HOSTS = ['*']

##### For Email ########
ACCOUNT_ACTIVATION_DAYS=15
EMAIL_HOST="smtp.gmail.com"
EMAIL_HOST_USER="colin.powell@gmail.com"
EMAIL_HOST_PASSWORD="hall6-jerkin"
DEFAULT_FROM_EMAIL="info@timberwyckfarm.com"
EMAIL_USE_TLS = True
