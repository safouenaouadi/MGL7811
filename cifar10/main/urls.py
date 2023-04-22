from django.conf.urls import url
from django.contrib import admin
from . import views
urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^predict$', views.predict, name='predict'),
    url(r'^correct$', views.correct, name='correct'),



]
