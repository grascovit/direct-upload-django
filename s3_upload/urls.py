from django.conf.urls import url
from .views import Home

urlpatterns = [
	url(r'^home/$', Home.as_view())
]
