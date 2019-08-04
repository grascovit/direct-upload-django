# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class S3UploadConfig(AppConfig):
    name = 's3_upload'
    verbose_name = 'S3 Upload'

    def ready(self):
        import s3_upload.signals # noqa
