from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^s3_upload/', include('s3_upload.urls', namespace='s3_upload')),
]
