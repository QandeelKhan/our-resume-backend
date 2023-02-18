# # https://our-space.nyc3.cdn.digitaloceanspaces.com/space-our-resume/media/blog-images/blog-img1.jpg
import os
from decouple import config
from OurResumeBackend.settings.common import BASE_DIR

USE_SPACES = config('USE_SPACES', cast=bool, default=False)

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / "space-our-resume/static"
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'space-our-resume/media'

if USE_SPACES:
    AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
    AWS_DEFAULT_ACL = 'public-read'
    AWS_S3_ENDPOINT_URL = config('AWS_S3_ENDPOINT_URL')
    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
    DEFAULT_FILE_STORAGE = 'OurResumeBackend.cdn.backends.MediaRootS3Boto3Storage'
    STATICFILES_STORAGE = 'OurResumeBackend.cdn.backends.StaticRootS3Boto3Storage'
else:
    DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'

    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'space-our-resume/static'),
    ]

    STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

    MEDIA_ROOT = os.path.join(BASE_DIR, 'space-our-resume/media')

    MEDIA_URL = '/media/'

    STATIC_ROOT = os.path.join(BASE_DIR, 'space-our-resume/static')

    STATIC_URL = '/static/'

# media settings
if USE_SPACES:
    MEDIA_URL = f'{AWS_S3_ENDPOINT_URL}/space-our-resume/media/'
else:
    MEDIA_URL = '/media/'

# static settings
if USE_SPACES:
    STATIC_URL = f'{AWS_S3_ENDPOINT_URL}/space-our-resume/static/'
else:
    STATIC_URL = '/static/'
