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
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'default',  # Replace with your actual database name
        'USER': 'harinduj93',  # Replace with your actual username
        'PASSWORD': 'admin123@',  # Replace with your actual password
        'HOST': 'harinduj93.mysql.pythonanywhere-services.com',  # Replace with your actual host address
        'PORT': '3306',  # Replace with your actual port (usually 3306 for MySQL)
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
ALLOWED_HOSTS = ['harinduj93.pythonanywhere.com']

