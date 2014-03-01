# Django settings for timberwyckfarm_com project.
import os, sys

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
PUBLIC_ROOT = os.path.join(PROJECT_ROOT, 'public')

MEDIA_ROOT = os.path.join(PUBLIC_ROOT, 'media/')
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(PUBLIC_ROOT, 'static/')
STATIC_URL = "/static/"

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static_files'),
)

DEBUG = True
TEMPLATE_DEBUG= DEBUG

# Django settings for twyck project.
ADMINS = (
    ('Colin Powell', 'colin.powell+twyck@gmail.com'),
)

USE_TZ = False  

LANGUAGES = [
    ('en', 'English'),
]

LANGUAGE_CODE = 'en-us'
MANAGERS = ADMINS
USE_I18N = True

TIME_ZONE = 'America/New_York'
SITE_ID = 1 

AUTH_PROFILE_MODULE='profiles.UserProfile'        

LOGIN_REDIRECT_URL = '/'

SECRET_KEY = 'lkjzx8*#IKJJKLSDKjsdfnmsl#h=b&!l7il%z4vj)hu3@cow%s'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.request',
    'django.core.context_processors.debug',
    'django.core.context_processors.media',
    'django.contrib.messages.context_processors.messages',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.csrf.CsrfResponseMiddleware',
    'onec_utils.middleware.SmartAppendSlashMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
)

AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend',)

ROOT_URLCONF = 'urls'

#HAYSTACK_SITECONF='search_sites'
#HAYSTACK_SEARCH_ENGINE='whoosh'
#HAYSTACK_WHOOSH_PATH=os.path.join(PROJECT_ROOT, 'search-index')

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.messages',
    'django.contrib.humanize',
    'django.contrib.comments',
    'django.contrib.admindocs',
    'django.contrib.sitemaps',
    'django.contrib.flatpages',

    'django_extensions',
    'debug_toolbar',
    'easy_thumbnails',
    'onec_utils',
    'markup_mixin',
    'typogrify',
    'attributes',
    'file_picker',
    'file_picker.uploads',
    'file_picker.wymeditor',

    'farm',
    'notes',
    'photologue',
 )

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        }
    }
}

from local_settings import *
