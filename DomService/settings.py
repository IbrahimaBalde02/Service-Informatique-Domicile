"""
Django settings for DomService project.
"""

from pathlib import Path
import os

# --- BASE DIRECTORY ---
BASE_DIR = Path(__file__).resolve().parent.parent


# --- SECURITY SETTINGS ---
SECRET_KEY = 'django-insecure-v8%gbh=oc3q#=1^4l-a5tsg!zz0*0to)tf7%=w_2#m7pco5ke5'
DEBUG = True
ALLOWED_HOSTS = []  # ➤ À modifier en production : ['tondomaine.com', '127.0.0.1']


# --- APPLICATIONS ---
INSTALLED_APPS = [
    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Tes apps
    'Services.apps.ServicesConfig',
    'widget_tweaks',
]


# --- MIDDLEWARE ---
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# --- URLS & WSGI ---
ROOT_URLCONF = 'DomService.urls'
WSGI_APPLICATION = 'DomService.wsgi.application'


# --- TEMPLATES ---
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # ✅ Dossier global des templates
        'DIRS': [], #BASE_DIR / 'templates'
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


# --- DATABASE ---
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# --- PASSWORD VALIDATION ---
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# --- LOCALISATION ---
LANGUAGE_CODE = 'fr'
TIME_ZONE = 'Africa/Conakry'
USE_I18N = True
USE_TZ = True


# --- STATIC FILES ---
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]  # Dossier global
STATIC_ROOT = BASE_DIR / "staticfiles"    # Pour collectstatic (prod)

# --- MEDIA FILES (si tu ajoutes des images plus tard) ---
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"

# Configuration de l’envoi d’emails
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'           # pour Gmail 
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'ibrahima.tounkisbalde@gmail.com'  # mon adresse email
EMAIL_HOST_PASSWORD = 'rgvr rrxo kjlq gvmj'  # ⚠️ mon mot de passe d’application Gmail/DomService
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


# --- AUTRES CONFIGS ---
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

