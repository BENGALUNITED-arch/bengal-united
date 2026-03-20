"""
Django settings for bengal_united project.
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
SECRET_KEY = 'django-insecure-4#f1^z!&u!l%=ag@!4@ys&^r7e%_o0y8wf&wx19@7ecuue!uka'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*'] # Allows all hosts for now, update with your domain later

# Application definition
INSTALLED_APPS = [
    'jazzmin',  # <-- THIS MAKES THE DASHBOARD PREMIUM (Must be first)
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # 🚀 OUR CUSTOM SAAS APPS 
    'core',
    'pages',
    'players',
    'news',
    'gallery',   # Media Gallery
    'trophies',  # Achievements
    'shop',      # E-Commerce
]

MIDDLEWARE = [
    'django.middleware.gzip.GZipMiddleware', # ⚡ SPEED BOOST: Compresses your website
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # 🌍 HOSTING: Serves static files
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bengal_united.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'bengal_united.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# --- STATIC FILES CONFIG (OPTIMIZED FOR SPEED) ---
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles' # Where files are collected for hosting

# WhiteNoise storage to compress and cache static files
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# --- MEDIA FILES CONFIG (USER UPLOADS) ---
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# ==========================================
# PREMIUM ADMIN DASHBOARD SETTINGS (JAZZMIN)
# ==========================================
JAZZMIN_SETTINGS = {
    "site_title": "Bengal United CMS",
    "site_header": "Bengal United Dashboard",
    "site_brand": "Bengal United",
    "site_logo": "core/img/logo.png", # Ensure you have a logo here or leave as brand text
    
    "welcome_sign": "Welcome to Bengal United Admin",
    "copyright": "Bengal United FC",
    
    "custom_css": "css/admin_custom.css",

    "topmenu_links": [
        {"name": "View Live Website", "url": "/", "new_window": True},
    ],

    "icons": {
        "core.SiteSettings": "fas fa-cog",
        "core.HeroSlide": "fas fa-images",
        "players.Player": "fas fa-users",
        "news.News": "fas fa-newspaper",
        "gallery.Album": "fas fa-camera-retro",
        "trophies.Trophy": "fas fa-trophy",
        "shop.Product": "fas fa-shopping-cart",
        "pages.About": "fas fa-info-circle",
        "pages.JoinSection": "fas fa-user-plus",
    },

    "order_with_respect_to": [
        "core", "pages", "players", "news", "gallery", "trophies", "shop",
    ],

    "show_sidebar": True,
    "navigation_expanded": True,
}

JAZZMIN_UI_TWEAKS = {
    "theme": "darkly",
    "dark_mode_theme": "darkly",
    "navbar": "navbar-dark",
    "sidebar": "sidebar-dark-primary",
    "brand_colour": "navbar-primary",
    "accent": "accent-primary",
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": True,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": True,
}