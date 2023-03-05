import os
import boto3
from decouple import config
from OurResumeBackend.settings.common import BASE_DIR

USE_SPACES = config('USE_SPACES', cast=bool, default=True)
# MEDIA_ROOT = BASE_DIR / 'space-our-resume/media'
if USE_SPACES:
    # settings
    AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
    AWS_DEFAULT_ACL = 'public-read'
    AWS_S3_ENDPOINT_URL = config('AWS_S3_ENDPOINT_URL')
    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}

    # create media directory if it doesn't exist
    s3 = boto3.resource('s3',
                        endpoint_url=AWS_S3_ENDPOINT_URL,
                        aws_access_key_id=AWS_ACCESS_KEY_ID,
                        aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    bucket = s3.Bucket(AWS_STORAGE_BUCKET_NAME)
    media_directory = 'space-our-resume/media'
    if not any(obj.key == media_directory + '/' for obj in bucket.objects.all()):
        bucket.put_object(Key=(media_directory + '/'))

    # static settings
    AWS_LOCATION = 'space-our-resume/static'
    STATIC_URL = f'https://our-space.nyc3.digitaloceanspaces.com/{AWS_LOCATION}/'
    STATICFILES_STORAGE = 'OurResumeBackend.cdn.backends.StaticStorage'

    # public media settings
    PUBLIC_MEDIA_LOCATION = 'space-our-resume/media'
    MEDIA_URL = f'https://our-space.nyc3.digitaloceanspaces.com/{PUBLIC_MEDIA_LOCATION}/'
    DEFAULT_FILE_STORAGE = 'OurResumeBackend.cdn.backends.MediaStorage'
else:
    STATIC_URL = '/static/'
    STATIC_ROOT = BASE_DIR / "space-our-resume/static"
    MEDIA_URL = '/media/'
    MEDIA_ROOT = BASE_DIR / 'space-our-resume/media'


STATICFILES_DIRS = (
    BASE_DIR / 'space-our-resume/static',
)

# helping material
# https://testdriven.io/blog/django-digitalocean-spaces/
# https://shopingly-space.fra1.digitaloceanspaces.com/media/productimg/0_98drx4MegZUq4iTd.jpeg
# python manage.py collectmedia --settings=OurResumeBackend.settings.production
