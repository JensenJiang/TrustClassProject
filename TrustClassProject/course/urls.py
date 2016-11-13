from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'(?P<courseID>[0-9]+)/p(?P<page>[0-9]+)$', views.coursePage),
    url(r'(?P<courseID>[0-9]+)/$', views.redirectToCoursePage),
]
