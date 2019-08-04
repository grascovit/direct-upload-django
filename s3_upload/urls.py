# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url, include
from rest_framework import routers
from .views import Home, GeneratePresignedS3Url, DocumentViewSet

router = routers.DefaultRouter()
router.register(r'documents', DocumentViewSet)

urlpatterns = [
	url(r'^', include(router.urls)),
	url(r'^home/$', Home.as_view(), name='home'),
	url(r'^generate_presigned_s3_url/$', GeneratePresignedS3Url.as_view(), name='generate_presigned_s3_url'),
]
