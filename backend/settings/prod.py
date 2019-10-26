from backend.settings.base import *
# AWS S3 연동 이후 작성
# WEBPACK_LOADER = {
#     'DEFAULT': {
#         'BUNDLE_DIR_NAME': 'bundles/',
#         'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.prod.json'),
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR+'/../', 'db.sqlite3'),
    }
}

ALLOWED_HOSTS = ['*']
