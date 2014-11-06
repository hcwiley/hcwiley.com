# Django settings for hcwiley_art project.
import os, sys
# Parse database configuration from $DATABASE_URL
import dj_database_url
if 'DATABASE_URL'in os.environ.keys():
  DATABASES = {}
  DATABASES['default'] =  dj_database_url.config()
else:
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
          'NAME': 'hcwiley_art',                      # Or path to database file if using sqlite3.
          'USER': 'django',
          'PASSWORD': 'django',
          'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
          'PORT': '',                      # Set to empty string for default.
          'OPTIONS': {
           "init_command": "SET foreign_key_checks = 0;",
      },
      }
  }

DEBUG = True
IS_DEV = True

if 'IS_DEV'in os.environ.keys():
  IS_DEV = os.environ['IS_DEV'] != 'False'
TEMPLATE_DEBUG = DEBUG

ADMINS = (
     ('H. Cole Wiley', 'cole@hcwiley.com'),
)

MANAGERS = ADMINS

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['*', 'hcwiley_art.art72.org', '.art72.org']

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(PROJECT_ROOT, '../collected-static')
STATIC_URL = '/static/'
if not IS_DEV:
  MEDIA_ROOT = '/home/hcwiley/webapps/hcwiley_art_media/'

#ADMIN_MEDIA_PREFIX = os.path.join(STATIC_URL, 'admin')
sys.path.append(PROJECT_ROOT)
sys.path.append(os.path.join(PROJECT_ROOT, 'hcwiley_art'))
 

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)

STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'assets'),
    os.path.join(PROJECT_ROOT, '../static/'),
)

# pipeline setup
STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'
PIPELINE_COMPILERS = (
    'pipeline.compilers.stylus.StylusCompiler',
)
#PIPELINE_ENABLED = True
if IS_DEV:
  PIPELINE_STYLUS_BINARY = '/usr/local/share/npm/bin/stylus'
  PIPELINE_YUGLIFY_BINARY = '/usr/local/share/npm/bin/yuglify'
  PIPELINE_UGLIFYJS_BINARY = '/usr/local/share/npm/lib/node_modules/yuglify/node_modules/uglify-js/bin/uglifyjs'
else:
  PIPELINE_STYLUS_BINARY =  '/home/hcwiley/webapps/front_stream/node_modules/.bin/stylus'
  PIPELINE_YUGLIFY_BINARY = '/home/hcwiley/webapps/front_stream/node_modules/.bin/yuglify'
  PIPELINE_UGLIFYJS_BINARY = '/home/hcwiley/webapps/front_stream/node_modules/yuglify/node_modules/uglify-js/bin/uglifyjs'

PIPELINE_CSS_COMPRESSOR = 'pipeline.compressors.yuglify.YuglifyCompressor'
PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.uglifyjs.UglifyJSCompressor'
PIPELINE_CSS = {
    'client': {
        'source_filenames': (
          'css/bootstrap.min.css',
          'css/index.styl',
        ),
        'output_filename': 'css/client.min.css',
        'extra_context': {
            'media': 'screen,projection',
        },
    },
}

PIPELINE_JS = {
    'client': {
        'source_filenames': (
          'js/jquery.js',
          'js/bootstrap.min.js',
          'js/jquery-ui-1.10.3.custom.min.js',
          'js/client.js',
        ),
        'output_filename': 'js/client.min.js',
    }
}
PIPELINE_ENABLED = not IS_DEV

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 't8a=&q*o7pa*allauuk#hwhmmckirk*=w6j&y5-2tmw7bnhe6q'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    ('pyjade.ext.django.Loader',(
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
        'django.template.loaders.eggs.Loader',
    )),
    
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'hcwiley_art.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'hcwiley_art.wsgi.application'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_admin_bootstrapped.bootstrap3',
    'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django_admin_bootstrapped',
    'django.contrib.webdesign',
    'tinymce',
    'pipeline',
    'south',
    'artist',
    'media_material',
)

TINYMCE_DEFAULT_CONFIG = {
    'theme': "advanced",
    'cleanup_on_startup': True,
}

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
