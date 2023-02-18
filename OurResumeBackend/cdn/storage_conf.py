# # https://our-space.nyc3.cdn.digitaloceanspaces.com/space-our-resume/media/blog-images/blog-img1.jpg
import os
from decouple import config
from OurResumeBackend.settings.common import BASE_DIR

USE_SPACES = config('USE_SPACES', cast=bool, default=False)

if USE_SPACES:
    AWS_ACCESS_KEY_ID = "DO00LF97WUUJ69Q639NQ"

    AWS_SECRET_ACCESS_KEY = "PGeiUJEJ+1bW75HfFu7kX3E2X2vZDDhpEJjnOJ42p/0"
    AWS_STORAGE_BUCKET_NAME = "our-space"
    # AWS_DEFAULT_ACL = 'public-read'
    AWS_S3_ENDPOINT_URL = "https://our-space.nyc3.digitaloceanspaces.com"
    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
    DEFAULT_FILE_STORAGE = 'OurResumeBackend.cdn.backends.MediaRootS3Boto3Storage'
    STATICFILES_STORAGE = 'OurResumeBackend.cdn.backends.StaticRootS3Boto3Storage'
    MEDIA_URL = f'{AWS_S3_ENDPOINT_URL}/space-our-resume/media/'
    STATIC_URL = f'{AWS_S3_ENDPOINT_URL}/space-our-resume/static/'
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
