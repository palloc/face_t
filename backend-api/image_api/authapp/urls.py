# config: utf-8
from django.conf.urls import url, include
from django.views.generic.base import *
from authapp import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^auth/$', views.face, name='auth')
]
