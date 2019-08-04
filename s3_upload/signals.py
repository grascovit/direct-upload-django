# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models.signals import post_delete
from django.dispatch import receiver

from .models import Document


@receiver(post_delete, sender=Document)
def delete_file_from_s3(sender, instance, *args, **kwargs):
    instance.attachment.delete(save=False)
