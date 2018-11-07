from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
	url(r'^$', views.callLoginForm, name='load_login'),
	url(r'^login/$', views.userLogin, name='login'),
    url(r'^devices/$', views.devices, name='devices'),
    url(r'^new_device/$', views.new_device, name='new_device'),
    url(r'^create_new_device/$', views.create_new_device, name='create_new_device'),
    url(r'^admin/', admin.site.urls),
	url(r'^relogin/$', views.userLogin, name='relogin'),
	url(r'^logout/$', views.userLogout, name='logout'),
    url(r'^(?P<device_ip>.+)/$', views.device_details, name='device_details')
]