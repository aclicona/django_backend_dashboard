import os
from decouple import config
from gqlauth.settings_type import GqlAuthSettings, email_field
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

# SECURITY WARNING: don't run with debug turned on in production!


DEBUG = config('DEBUG', default=False, cast=bool)

SECRET_KEY = config('SECRET_KEY')
ADMINS = [('Andres', 'aclicona@gmail.com'), ('Giovanny', 'gcasas.est@gmail.com')]

INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
    'django_vite',
    'corsheaders',
    'tinymce',
    # 'adminsortable',
    "strawberry_django",
    "gqlauth",

    'versatileimagefield',
    'django_filters',
    'graphene_django',
    'django_cleanup.apps.CleanupConfig',
    'reset_migrations',
    'backend.apps.core',
    'backend.apps.account',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'backend.apps.core.middleware.jwt_refresh_token_middleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'gqlauth.core.middlewares.django_jwt_middleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
    'compression_middleware.middleware.CompressionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]
TINYMCE_DEFAULT_CONFIG = {
    "height": "320px",
    "width": "960px",
    "menubar": "file edit view insert format tools table help",
    "plugins": "advlist autolink lists link image charmap print preview anchor searchreplace visualblocks code "
               "fullscreen insertdatetime media table paste code help wordcount ",
    "toolbar": "undo redo | bold italic underline strikethrough | fontselect fontsizeselect formatselect | alignleft "
               "aligncenter alignright alignjustify | outdent indent |  numlist bullist checklist | forecolor "
               "backcolor casechange permanentpen formatpainter removeformat | pagebreak | charmap emoticons | "
               "fullscreen  preview save print | insertfile image media pageembed template link anchor codesample | "
               "a11ycheck ltr rtl | showcomments addcomment code",
    "custom_undo_redo_levels": 10,
}

ROOT_URLCONF = 'backend.urls'

WSGI_APPLICATION = 'backend.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': '',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
AUTH_USER_MODEL = "account.User"
# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

# STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# GRAPHENE = {
#     "SCHEMA": "backend.apps.graph.schema.schema",
#     "MIDDLEWARE": (
#         "graphql_jwt.middleware.JSONWebTokenMiddleware",
#         "graphene_django.debug.DjangoDebugMiddleware",
#     ),
#     # "SCHEMA_OUTPUT": "schema.graphql",
#     # "SCHEMA_INDENT": 2,
# }

AUTHENTICATION_BACKENDS = [
    'graphql_jwt.backends.JSONWebTokenBackend',
    'django.contrib.auth.backends.ModelBackend',
]

GRAPHQL_JWT = {
    "JWT_ALLOW_ANY_CLASSES": [
        "graphql_auth.mutations.Register",
        "graphql_auth.mutations.VerifyAccount",
        "graphql_auth.mutations.ObtainJSONWebToken",
        "graphql_auth.mutations.RefreshToken",
        "graphql_auth.mutations.RevokeToken",
    ],
    "JWT_VERIFY_EXPIRATION": True,
    "JWT_LONG_RUNNING_REFRESH_TOKEN": True,
    'JWT_EXPIRATION_DELTA': timedelta(minutes=10),
    'JWT_REFRESH_EXPIRATION_DELTA': timedelta(days=5),
    'JWT_REUSE_REFRESH_TOKENS': True,

}
GQL_AUTH = GqlAuthSettings(
    LOGIN_REQUIRE_CAPTCHA=False,
    REGISTER_REQUIRE_CAPTCHA=False,
    REGISTER_MUTATION_FIELDS={email_field},
    LOGIN_FIELDS={email_field},
    ALLOW_LOGIN_NOT_VERIFIED=True
)

# GRAPHQL_AUTH = {
#     'USERNAME_FIELD': ['email'],
#     'LOGIN_ALLOWED_FIELDS': ['email'],
#     'USER_NODE_FILTER_FIELDS': {
#         "email": ["exact", ],
#
#         "is_active": ["exact"],
#         "status__archived": ["exact"],
#         "status__verified": ["exact"],
#         "status__secondary_email": ["exact"],
#     },
#     'REGISTER_MUTATION_FIELDS': ['email', 'first_name'],
#     'REGISTER_MUTATION_FIELDS_OPTIONAL': ['email'],
#     'EMAIL_TEMPLATE_PASSWORD_RESET': "mails/account_password_reset_email.html",
#     'EMAIL_TEMPLATE_ACTIVATION': "mails/account_activation_email.html",
#     'EMAIL_SUBJECT_ACTIVATION': "mails/account_activation_subject.txt",
#     'EMAIL_SUBJECT_PASSWORD_RESET': "mails/account_password_reset_subject.txt",
#     "SEND_ACTIVATION_EMAIL": False,
#     "ACTIVATION_PATH_ON_EMAIL": config('ACTIVATION_PATH_ON_EMAIL', default="cuenta/activar"),
#     "PASSWORD_RESET_PATH_ON_EMAIL": config('PASSWORD_RESET_PATH_ON_EMAIL', default="cuenta/password-reset"),
#     "ALLOW_LOGIN_NOT_VERIFIED": config('ALLOW_LOGIN_NOT_VERIFIED', default=True),
#     "EXPIRATION_PASSWORD_RESET_TOKEN": config('EXPIRATION_PASSWORD_RESET_TOKEN', default=timedelta(hours=12)),
# }
#
VERSATILEIMAGEFIELD_RENDITION_KEY_SETS = {
    "background_images": [("header_image", "thumbnail__1080x440")],
    "user_avatars": [("default", "thumbnail__445x445")],
}

PLACEHOLDER_IMAGES = {
    60: "images/placeholder60x60.png",
    120: "images/placeholder120x120.png",
    255: "images/placeholder255x255.png",
    540: "images/placeholder540x540.png",
    1080: "images/placeholder1080x1080.png",
}
VERSATILEIMAGEFIELD_USE_PLACEHOLDIT = True
# Definir si las imágenes de los productos van a ser redimensionadas a una imagen cuadrada
PRODUCT_SQUARED_IMAGES = config('PRODUCT_SQUARED_IMAGES', default=True)

MAX_IMAGE_HEIGHT_OR_WIDTH = config('MAX_IMAGE_HEIGHT_OR_WIDTH', default=max(list(PLACEHOLDER_IMAGES.keys())))

FRONTEND_SCHEME = 'http'
FRONTEND_HOST = config('FRONTEND_HOST', default='127.0.0.1:8000', cast=str)
SITE_NAME = 'Micrositio UGC'
