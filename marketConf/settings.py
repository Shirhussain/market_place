from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@=-bhle3$1#+5sl)g4ow0_hk!lb$d(ih3@(qk(gwr2&lhp&rcc'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    #myapp
    'market.apps.MarketConfig',
    'account.apps.AccountConfig',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #third party
    "bootstrap4",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'marketConf.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'marketConf.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/


"""This line tells Django to append static to the base url
(in our case localhost:8000) when searching for static files. 
In Django, you could have a static folder almost anywhere you want. 
You can even have more than one static folder e.g. one in each app.
"""
STATIC_URL = '/static/'

#The STATICFILES_DIRS tuple tells Django where to look for static files that are not tied to a particular app. 
#In this case, we just told Django to also look for static files in a folder called static in our root folder, 
#not just in our apps.
STATICFILES_DIRS = [BASE_DIR / 'static']


"""
Django also provides a mechanism for collecting static files into one place so that they can be served easily. 
Using the collectstatic command, Django looks for all static files in your apps and collects them wherever you told it to,
i.e. the STATIC_ROOT. In our case, we are telling Django that when we run python manage.py collectstatic, 
gather all static files into a folder called staticfiles in our project root directory. 
This feature is very handy for serving static files, especially in production settings.
"""
STATIC_ROOT = BASE_DIR / 'static_root'


MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'




#login redirect
LOGIN_REDIRECT_URL = '/'



#Email Pasword reset
EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = BASE_DIR / 'app-message' # change this to a proper location

