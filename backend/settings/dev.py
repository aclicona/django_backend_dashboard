from .settings import *

DEBUG = config('DEBUG', default=True, cast=bool)
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '.herokuapp.com']
CORS_ORIGIN_ALLOW_ALL = DEBUG
# WEBPACK_LOADER = {
#     'DEFAULT': {
#         'BUNDLE_DIR_NAME': '',
#         'STATS_FILE': os.path.join(BASE_DIR, 'dashboard/webpack-stats.json'),
#     }
# }
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
MEDIA_URL = '/dmedia/'
MEDIA_ROOT = os.path.join(BASE_DIR, "mediafiles")

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")


VUE_ROOT = os.path.join(BASE_DIR, "dashboard")
DJANGO_VITE_DEV_MODE = DEBUG  # Set to False in production
DJANGO_VITE_DEV_SERVER_PROTOCOL = 'http'
DJANGO_VITE_DEV_SERVER_HOST = 'localhost'
DJANGO_VITE_DEV_SERVER_PORT = 3000

DEBUG_TOOLBAR_CONFIG = {
    # Toolbar options
    'RESULTS_CACHE_SIZE': 3,
    'SHOW_COLLAPSED': True,
    # Panel options
    'SQL_WARNING_THRESHOLD': 100,   # milliseconds
}
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), VUE_ROOT],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.static',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'libraries': {
                'my_tags': 'backend.apps.core.templatetags.template_tags',
            },
        },
    },
]
INTERNAL_IPS = (
    '127.0.0.1',
    'localhost'
)

VERSATILEIMAGEFIELD_SETTINGS = {
    # Images should be pre-generated on Production environment
    "create_images_on_demand": config('CREATE_IMAGES_ON_DEMAND', default=DEBUG)
}
