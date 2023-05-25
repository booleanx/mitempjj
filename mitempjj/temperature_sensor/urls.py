"""temperature_sensor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from temperature_sensor.views import *
#for auth:
from django.contrib.auth import views as auth_views
from django.urls import path, re_path
from django.conf.urls import include

from jchart import Chart
urlpatterns = [
    re_path (r'^admin/', admin.site.urls),
    re_path (r'temperature_sensor/$', temperature_sensor_view, name='temperature_sensor'),
    re_path (r'temperature_sensor2/$', temperature_sensor_view2, name='temperature_sensor2'),
    re_path (r'temperature/$', temperature_sensor_viewbytype, name='temperature'),
    path('temperature_sensor/api/', MitempApiView.as_view()),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'),name='logout'),
    re_path (r'', main_view, name="main"),
]


urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]