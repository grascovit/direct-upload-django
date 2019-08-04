# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import boto3
from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED

from direct_upload.settings import (AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY,
                                    AWS_STORAGE_BUCKET_NAME)

from .models import Document
from .serializers import DocumentSerializer


class Home(TemplateView):
    template_name = 'home.html'


class GeneratePresignedS3Url(View):
    def get(self, request):
        session = boto3.session.Session(
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY
        )
        client = session.client('s3')
        presigned_post_data = client.generate_presigned_post(
            Bucket=AWS_STORAGE_BUCKET_NAME,
            Key=request.GET.get('name'),
            Fields={'Content-Type': request.GET.get('type')},
            Conditions=[
                {'Content-Type': request.GET.get('type')}
            ]
        )

        return JsonResponse(presigned_post_data)


class DocumentViewSet(viewsets.ModelViewSet):
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()
    permission_classes = []
    http_method_names = ['get', 'post', 'delete']

    def create(self, request, *args, **kwargs):
        document = Document.objects.create(attachment=request.data.get('attachment'))
        serializer = self.get_serializer(document)

        return Response(serializer.data, status=HTTP_201_CREATED)
