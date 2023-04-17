from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class PublicMediaStorage(S3Boto3Storage):
    location = 'erpfiles'
    default_acl = 'public-read'
    file_overwrite = True