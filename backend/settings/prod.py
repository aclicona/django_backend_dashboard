from .settings import *
DEBUG = config('DEBUG', default=True)

ALLOWED_HOSTS = ['*']
STATIC_HOST = config('CDN_STATIC_HOST', default='')
# WEBPACK_LOADER = {
#     'DEFAULT': {
#         'BUNDLE_DIR_NAME': '' if STATIC_HOST == '' else '/',
#         'STATS_FILE': os.path.join(BASE_DIR, 'dashboard/webpack-stats-prod.json'),
#     }
# }

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

MEDIA_URL = '/dmedia/'
MEDIA_ROOT = os.path.join(BASE_DIR, "mediafiles")

STATIC_URL = STATIC_HOST + '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]
# DJANGO_VITE_ASSETS_PATH = 'path/to/your/vite/project/dist'
DJANGO_VITE_DEV_MODE = DEBUG  # Set to False in production
VUE_ROOT = os.path.join(BASE_DIR, "dashboard/dist/")

DJANGO_VITE_MANIFEST_PATH = VUE_ROOT + 'manifest.json'

CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000'
]
# DEBUG = True
FRONTEND_HOST = config('FRONTEND_HOST', default=None)
if FRONTEND_HOST is not None:
    CORS_ALLOWED_ORIGINS.append(FRONTEND_HOST)
ALLOWED_CLIENT_HOSTS = 'localhost, 127.0.0.1, 10.4.36.94'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), os.path.join(BASE_DIR, 'dashboard')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
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

# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# SECURE_SSL_REDIRECT = True
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True

# AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID', default=None)
# AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY', default=None)
# AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME', default=None)
# AWS_DEFAULT_ACL = 'public-read'
# AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
# AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
# MEDIA_ROOT = 'media'
# MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIA_ROOT}/"

# AWS_PUBLIC_MEDIA_LOCATION = 'media/public'
# DEFAULT_FILE_STORAGE = 'backend.storage_backends.PublicMediaStorage'

# AWS_PRIVATE_MEDIA_LOCATION = 'media/private'
# PRIVATE_FILE_STORAGE = 'backend.storage_backends.PrivateMediaStorage'

VERSATILEIMAGEFIELD_SETTINGS = {
    # Images should be pre-generated on Production environment
    "create_images_on_demand": config('CREATE_IMAGES_ON_DEMAND', default=False)
}