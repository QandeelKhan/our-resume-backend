import os
from pathlib import Path
from decouple import config
from dotenv import load_dotenv
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

USE_SPACES = config('USE_SPACES', cast=bool, default=True)

if USE_SPACES:
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_ENDPOINT_URL = os.getenv('AWS_S3_ENDPOINT_URL')
    AWS_DEFAULT_ACL = 'public-read'
    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}

    DEFAULT_FILE_STORAGE = 'OurResumeBackend.cdn.backends.S3Boto3Storage'
    MEDIA_URL = f"https://{AWS_STORAGE_BUCKET_NAME}.{AWS_S3_ENDPOINT_URL}/space-our-resume/media/"
    STATIC_URL = f"https://{AWS_STORAGE_BUCKET_NAME}.{AWS_S3_ENDPOINT_URL}/space-our-resume/static/"
    STATIC_ROOT = BASE_DIR / "space-our-resume/staticfiles"
else:
    MEDIA_URL = '/media/'
    MEDIA_ROOT = BASE_DIR / 'space-our-resume/media/'
    STATIC_URL = '/static/'
    STATICFILES_DIRS = [BASE_DIR / 'static']
    STATIC_ROOT = BASE_DIR / "space-our-resume/static/"

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]
