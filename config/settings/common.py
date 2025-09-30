# -*- coding: utf-8 -*-
"""
Django settings for law project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""
from __future__ import absolute_import, unicode_literals

import environ

ROOT_DIR = environ.Path(__file__) - 3  # (/a/b/myfile.py - 3 = /)
APPS_DIR = ROOT_DIR.path('law')

env = environ.Env()
environ.Env.read_env(str(ROOT_DIR.path('.env')))

# APP CONFIGURATION
# ------------------------------------------------------------------------------
DJANGO_APPS = (
    # Default Django apps:
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',

    # Useful template tags:
    # 'django.contrib.humanize',

    # Admin
    'django.contrib.admin',
)
THIRD_PARTY_APPS = (
    'django_extensions',
    'crispy_forms',  # Form layouts
    'crispy_bootstrap4',  # Bootstrap 4 Form layouts
    'crispy_forms_foundation',  # Zurb Foundation Form layouts
    'allauth',  # registration
    'allauth.account',  # registration
    'allauth.socialaccount',  # registration
    'mptt',  # Tree traversal
    'colorfield',  # django color field
    'ckeditor',
    # 'bidiutils',  # Removed: not a Django app
    'easy_thumbnails',
    'embed_video',
    # 'law.core.apps_overrides.FilebrowserConfig',  # Removed: not compatible with Django 4.x/3.12
    # 'admin_reorder',  # Removed: not compatible with Django 4.x/3.12
    'analytical',
    'django_cleanup',
    # 'django_unused_media',  # Removed: not available for Django 4.x/Python 3.12
    # 'capture_tag',  # Removed: not available for Django 4.x/Python 3.12
    'mailer',
)

# Apps specific for this project go here.
LOCAL_APPS = (
    'law.users.apps.UsersConfig',  # custom users app
    # Your stuff: custom apps go here
    'law.core',
    'law.importer',
    'law.links.apps.LinksConfig',
    'law.contributors.apps.ContributorsConfig',
    'law.content.apps.ContentConfig',
    'law.pages.apps.PagesConfig',
    'law.photos.apps.PhotosConfig',
    'law.search',
    'law.contact.apps.ContactConfig',
    'law.mailinglists.apps.MailingListsConfig',
    'law.rss',
    'law.lawyers.apps.LawyersConfig',
    'law.practices.apps.AppConfig',
    'law.knowledge.apps.KnowledgeConfig',
    'law.about_sidebar.apps.AboutSidebarConfig',
    'law.annotations.apps.AnnotationsConfig',
    'law.redirects.apps.RedirectsConfig',
    'law.seo.apps.SeoConfig',
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# MIDDLEWARE CONFIGURATION
# ------------------------------------------------------------------------------
MIDDLEWARE = [
    # Make sure djangosecure.middleware.SecurityMiddleware is listed first
    'django.contrib.sessions.middleware.SessionMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    # 'solid_i18n.middleware.SolidLocaleMiddleware',  # Removed for Django 4.x compatibility
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # 'admin_reorder.middleware.ModelAdminReorder',  # Removed: not compatible with Django 4.x/3.12
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'law.redirects.middleware.URLRedirectsMiddleware',
]

# MIGRATIONS CONFIGURATION
# ------------------------------------------------------------------------------
MIGRATION_MODULES = {
    'sites': 'law.contrib.sites.migrations'
}

# DEBUG
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = env.bool("DJANGO_DEBUG", False)

# FIXTURE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-FIXTURE_DIRS
FIXTURE_DIRS = (
    str(APPS_DIR.path('fixtures')),
)

# EMAIL CONFIGURATION
# ------------------------------------------------------------------------------
EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND',
                    default='mailer.backend.DbBackend')

# MANAGER CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = (
    ("""Meir Kriheli""", 'mkriheli@gmail.com'),
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS

# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    # Raises ImproperlyConfigured exception if DATABASE_URL not in os.environ
    'default': env.db('DATABASE_URL', default='postgres:///law'),
    # 'legacy': env.db('LEGACY_DB_URL', default='mysql://localhost/wwwlawcoil'),
}
DATABASES['default']['ATOMIC_REQUESTS'] = True

DATABASE_ROUTERS = ['law.importer.dbroute.LegacyRouter']


# GENERAL CONFIGURATION
# ------------------------------------------------------------------------------
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Israel'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = 'he'

# See: https://docs.djangoproject.com/en/idev/ref/settings/#languages
from django.utils.translation import gettext_lazy as _

LANGUAGES = (
    ('he', _('Hebrew')),
    ('en', _('English')),
)

LOCALE_PATHS = [
    ROOT_DIR('config', 'settings', 'locale'),
]

# See: https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True

# TEMPLATE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES = [
    {
        # See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-TEMPLATES-BACKEND
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
        'DIRS': [
            str(APPS_DIR.path('templates')),
        ],
        'OPTIONS': {
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
            'debug': DEBUG,
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
            # https://docs.djangoproject.com/en/dev/ref/templates/api/#loader-types
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                # Your stuff: custom template context processors go here
                # 'bidiutils.context_processors.bidi',  # Removed: not compatible with Python 3.12
            ],
        },
    },
]

# See: http://django-crispy-forms.readthedocs.org/en/latest/install.html#template-packs
CRISPY_ALLOWED_TEMPLATE_PACKS = ('bootstrap', 'uni_form', 'bootstrap3', 'foundation-5', 'bootstrap4')
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# STATIC FILE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = str(ROOT_DIR('staticfiles'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = '/static/'

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = (
    str(APPS_DIR.path('static')),
)

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# MEDIA CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = str(APPS_DIR('media'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'

# URL Configuration
# ------------------------------------------------------------------------------
ROOT_URLCONF = 'config.urls'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = 'config.wsgi.application'

# AUTHENTICATION CONFIGURATION
# ------------------------------------------------------------------------------
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

# Some really nice defaults
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'none'

# Custom user app defaults
# Select the correct user model
AUTH_USER_MODEL = 'users.User'
LOGIN_REDIRECT_URL = 'users:redirect'
LOGIN_URL = 'account_signup'

# SLUGLIFIER
AUTOSLUG_SLUGIFY_FUNCTION = 'slugify.slugify'


# Location of root django.contrib.admin URL, use {% url 'admin:index' %}
ADMIN_URL = r'^admin/'

# Message storage backend, see:
# https://docs.djangoproject.com/en/1.10/ref/settings/#std:setting-MESSAGE_STORAGE
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

# Your common stuff: Below this line define 3rd party library settings
PASSWORD_ENC_KEY = env('PASSWORD_ENC_KEY')

OLD_LAW_CO_IL = 'http://law.co.il'

MPTT_ADMIN_LEVEL_INDENT = 20

# Items per page when number of items for all pages is equal
ITEMS_PER_PAGE = 6

# Items per page when number of items for 1st page is different than the rest
ITEMS_FOR_FIRST_PAGE = 7
ITEMS_FOR_REST_OF_PAGES = 8

# Items for hot_topics
ITEMS_FOR_REST_OF_HOT_TOPICS = 4

THUMBNAIL_ALIASES = {
    'law.photos.WidePhoto.photo': {'size': (582, 420), 'crop': True},
    'law.photos.NarrowPhoto.photo': {'size': (269, 615), 'crop': True},
}

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'width': 850,
        'allowedContent': True,
        'toolbar_Custom': [
            ['Format'],
            ['Bold', 'Italic', 'Underline', 'SpecialChar'],
            ['Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo'],
            ['Link', 'Unlink', 'Anchor'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent'],
            ['Image', 'Table', 'HorizontalRule'],
            ['TextColor', 'BGColor'],
            ['Source'],
        ],
    }
}

# File Browser in admin
# ------------------------------------------------------------------------------
# See: https://github.com/smacker/django-filebrowser-no-grappelli
FILEBROWSER_DIRECTORY = ''
FILEBROWSER_EXTENSIONS = {
    'Image': ['.jpg', '.jpeg', '.gif', '.png', '.tif', '.tiff'],
    'Document': ['.pdf', '.doc', '.rtf', '.txt', '.xls', '.csv',
                 '.docx', '.xlsx', '.ppt', 'pptx', '.odt', '.ods', '.odp'],
    'Video': ['.mov', '.wmv', '.mpeg', '.mpg', '.avi', '.rm'],
    'Audio': ['.mp3', '.mp4', '.wav', '.aiff', '.midi', '.m4p']
}


# Order of models in the admin
# ------------------------------------------------------------------------------
# See: https://github.com/mishbahr/django-modeladmin-reorder
ADMIN_REORDER = (
    'content',
    'links',
    'mailinglists',
    'knowledge',
    'photos',
    {
        'label': _('General'),
        'app': 'contributors',
        'models': (
            'contributors.Contributor',
            'filebrowser.FileBrowser',
            'contact.FeedbackMessage',
        )
    },
    {
        'label': _('About site'),
        'app': 'practices',
        'models': (
            'practices.PracticeArea',
            'lawyers.Lawyer',
            'pages.Page',
            'redirects.Redirects',
        )
    },
    'users',
    'mailer',
)

# Recepients for feedback messages
CONTACTS_RECIPIENTS = (
    ("""Haim Ravia""", 'ravia@law.co.il'),
)

# ANALYTICS

GOOGLE_ANALYTICS_PROPERTY_ID = 'UA-280314-2'
GOOGLE_ANALYTICS_ANONYMIZE_IP = True

PIWIK_DOMAIN_PATH = 'analytics.law.co.il'
PIWIK_SITE_ID = '1'


# Mailer config
MAILER_EMAIL_MAX_BATCH = env.int('DJANGO_MAILER_MAX_BATCH', 100)
MAILER_EMAIL_MAX_DEFERRED = env.int('DJANGO_MAILER_MAX_DEFERRED', 2)
MAILER_EMAIL_THROTTLE = env.int('DJANGO_MAILER_THROTTLE', 1)
