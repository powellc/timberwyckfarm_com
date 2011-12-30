# Django settings for maplepepper_com project.
import os
import sys
import warnings; warnings.simplefilter("ignore")

## Directories
PROJECT_ROOT = os.path.dirname(os.path.realpath(os.path.dirname(__file__)))
SITE_ROOT = os.path.dirname(PROJECT_ROOT)
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media/')

VIRTUALENV='/var/lib/virtualenvs/twyck/lib/python2.5/site-packages'

sys.path.append(SITE_ROOT)

DEBUG = True
TEMPLATE_DEBUG= DEBUG

# Django settings for twyck project.
ADMINS = (
    ('Colin Powell', 'colin@onecardinal.com'),
)

LANGUAGE_CODE = 'en-us'
MANAGERS = ADMINS
USE_I18N = True

APPEND_SLASH=False
SMART_APPEND_SLASH=True

SEND_BROKEN_LINK_EMAILS=True
#IGNORABLE_404_STARTS=('',)

TIME_ZONE = 'America/New_York'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1 

import logging

LOG_DATE_FORMAT = '%d %b %Y %H:%M:%S'
LOG_FORMATTER = logging.Formatter('%(asctime)s %(name)-7s: %(levelname)-8s %(message)s',
    datefmt=LOG_DATE_FORMAT)

FILE_HANDLER = logging.FileHandler(os.path.join(PROJECT_ROOT)+'/django.log', 'w')
CONSOLE_HANDLER = logging.StreamHandler() # defaults to stderr
CONSOLE_HANDLER.setFormatter(LOG_FORMATTER)
CONSOLE_HANDLER.setLevel(logging.DEBUG)

AUTH_PROFILE_MODULE='profiles.UserProfile'        

LOGIN_REDIRECT_URL = '/'

SECRET_KEY = 'v0%26bx!p-uv1lvj_kuvk%cz+8h=b&!l7il%z4vj)hu3@cow%s'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.request',
    'django.core.context_processors.debug',
    'django.core.context_processors.media',
    'django.contrib.messages.context_processors.messages',)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.csrf.CsrfResponseMiddleware',
    'onec_utils.middleware.SmartAppendSlashMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend',)

ROOT_URLCONF = 'urls'
HAYSTACK_SITECONF='pbp_com.search_sites'
HAYSTACK_SEARCH_ENGINE='whoosh'
HAYSTACK_WHOOSH_PATH=os.path.join(PROJECT_ROOT, 'search-index')

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.markup',
    'django.contrib.humanize',
    'django.contrib.comments',
    'django.contrib.admindocs',
    'django.contrib.sitemaps',
    'django.contrib.flatpages',

    'django_extensions',
#    'debug_toolbar',
    'easy_thumbnails',
    'onec_utils',
    'markup_mixin',
    'typogrify',
    'attributes',
    'file_picker',
    'file_picker.uploads',
    'file_picker.wymeditor',

    'wiki',
    'articles',
    'farm',
    'notes',
    'photologue',
 )


