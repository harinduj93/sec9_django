from pathlib import Path
import dj_database_url
# Define the base directory of your project
BASE_DIR = Path(__file__).resolve().parent.parent

INSTALLED_APPS = [
    # Other installed apps,
    'store',
    'django.contrib.auth',
    'django.contrib.contenttypes',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
DEBUG = False
ALLOWED_HOSTS = ['your-heroku-app.herokuapp.com']



DATABASES = {
    'default': dj_database_url.config(default='postgres://localhost/mydb')
}
