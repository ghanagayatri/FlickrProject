from django.conf.urls import patterns, url
from flickrMap import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'))
