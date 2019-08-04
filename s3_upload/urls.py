# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import include, url
from rest_framework import routers

from .views import DocumentViewSet, GeneratePresignedS3Url, Home

router = routers.DefaultRouter()
router.register(r'documents', DocumentViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^home/$', Home.as_view(), name='home'),
    url(r'^generate_presigned_s3_url/$', GeneratePresignedS3Url.as_view(), name='generate_presigned_s3_url'),
]
