import os
from decouple import config
from OurResumeBackend.settings.common import BASE_DIR
from dotenv import load_dotenv
load_dotenv()


USE_SPACES = config('USE_SPACES', cast=bool, default=True)

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")
print(AWS_STORAGE_BUCKET_NAME)
AWS_S3_ENDPOINT_URL = os.getenv("AWS_S3_ENDPOINT_URL")
AWS_DEFAULT_ACL = "public-read"
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}


if USE_SPACES:
    # DigitalOcean Spaces settings
    # DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    # # DEFAULT_FILE_STORAGE = 'OurResumeBackend.cdn.backends.MediaRootS3Boto3Storage'
    # # STATICFILES_STORAGE = 'OurResumeBackend.cdn.backends.StaticRootS3Boto3Storage'

    # Use DigitalOcean Spaces for static and media files
    # STATICFILES_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
    STATICFILES_STORAGE = 'OurResumeBackend.cdn.backends.StaticRootS3Boto3Storage'
    # DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
    DEFAULT_FILE_STORAGE = 'OurResumeBackend.cdn.backends.MediaRootS3Boto3Storage'

    # Custom domain for serving static files from Spaces
    # AWS_S3_CUSTOM_DOMAIN = f"https://{AWS_STORAGE_BUCKET_NAME}.{AWS_S3_ENDPOINT_URL}"
    # print(AWS_S3_CUSTOM_DOMAIN)

    # Static file settings
    # STATIC_URL = f"{AWS_S3_ENDPOINT_URL}/our-space/space-our-resume/"
    STATIC_URL = 'https://our-space.nyc3.digitaloceanspaces.com/our-space/space-our-resume/'
    print(STATIC_URL)
    STATIC_ROOT = None

    # Media file settings
    MEDIA_URL = f"{AWS_S3_ENDPOINT_URL}/space-our-resume/media/"
    MEDIA_ROOT = None
    STATICFILES_STORAGE = DEFAULT_FILE_STORAGE
    # Django storage settings
    AWS_LOCATION = 'space-our-resume'  # set to a subdirectory if desired
    STATICFILES_LOCATION = 'space-our-resume/static'
    MEDIAFILES_LOCATION = 'space-our-resume/media'
else:
    # Django default storage settings
    # DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'space-our-resume/media')
    STATIC_ROOT = os.path.join(BASE_DIR, 'space-our-resume/static')
    MEDIA_URL = '/media/'
    STATIC_URL = '/static/'

# cache settings
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = 'public-read'
AWS_QUERYSTRING_EXPIRE = 3600
