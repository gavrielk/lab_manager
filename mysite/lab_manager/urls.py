from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.create_new_device, name='new device'),
    url(r'^admin/', admin.site.urls),
]