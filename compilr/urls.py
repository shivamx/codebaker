from django.conf.urls import patterns, url
from compilr import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'))