from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'p(?P<page>[0-9]+)$', views.homePage),
    url(r'$', views.redirectToHomePage),
]
