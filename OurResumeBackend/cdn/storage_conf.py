import os
from decouple import config
# from StrefrontBackend2.settings import BASE_DIR
from ..settings.common import BASE_DIR

USE_SPACES = config('USE_SPACES', cast=bool, default=False)

if USE_SPACES:
    # settings
    AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
    AWS_DEFAULT_ACL = 'public-read'
    AWS_S3_ENDPOINT_URL = config('AWS_S3_ENDPOINT_URL')
    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
    # static settings
    # AWS_LOCATION = 'space-our-resume/static'
    # STATIC_URL = f'https://our-space.nyc3.digitaloceanspaces.com/{AWS_LOCATION}'
    # public media settings
    PUBLIC_MEDIA_LOCATION = 'space-our-resume/media'
    # MEDIA_URL = f'https://our-space.nyc3.digitaloceanspaces.com/{PUBLIC_MEDIA_LOCATION}'

    AWS_LOCATION = f'https://our-space.nyc3.digitaloceanspaces.com'
    DEFAULT_FILE_STORAGE = 'OurResumeBackend.cdn.backends.MediaRootS3Boto3Storage'
    STATICFILES_STORAGE = 'OurResumeBackend.cdn.backends.StaticRootS3Boto3Storage'
    STATIC_URL = '/static/'
    STATIC_ROOT = BASE_DIR / "space-our-resume/static"
    MEDIA_URL = '/media/'
    MEDIA_ROOT = BASE_DIR / 'space-our-resume/media'
else:
    STATIC_URL = '/static/'
    STATIC_ROOT = BASE_DIR / "space-our-resume/static"
    MEDIA_URL = '/media/'
    MEDIA_ROOT = BASE_DIR / 'space-our-resume/media'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'space-our-resume/'),
]
# helping material
# https://testdriven.io/blog/django-digitalocean-spaces/
# https://our-space.nyc3.digitaloceanspaces.com
