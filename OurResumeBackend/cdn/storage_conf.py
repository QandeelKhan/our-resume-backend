import os
from decouple import config
from OurResumeBackend.settings.common import BASE_DIR

USE_SPACES = config('USE_SPACES', cast=bool, default=True)

if USE_SPACES:
    # settings
    AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
    AWS_DEFAULT_ACL = 'public-read'
    AWS_S3_ENDPOINT_URL = config('AWS_S3_ENDPOINT_URL')
    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
    # static settings
    AWS_LOCATION = 'space-shoppingly/static'
    STATIC_URL = f'https://our-space.nyc3.digitaloceanspaces.com/{AWS_LOCATION}/'
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    # public media settings
    PUBLIC_MEDIA_LOCATION = 'space-our-resume/media'
    MEDIA_URL = f'https://our-space.nyc3.digitaloceanspaces.com/{PUBLIC_MEDIA_LOCATION}/'

    DEFAULT_FILE_STORAGE = 'OurResumeBackend.cdn.backends.MediaRootS3Boto3Storage'
else:
    STATIC_URL = '/static/'
    STATICFILES_DIRS = (
        BASE_DIR / 'space-shoppingly/static',
    )
    STATIC_ROOT = BASE_DIR / "staticfiles"
    MEDIA_URL = '/media/'
    MEDIA_ROOT = BASE_DIR / 'space-shoppingly/media'

# helping material
# https://testdriven.io/blog/django-digitalocean-spaces/
# https://shopingly-space.fra1.digitaloceanspaces.com/media/productimg/0_98drx4MegZUq4iTd.jpeg
