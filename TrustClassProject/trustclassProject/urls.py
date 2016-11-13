"""trustclassProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
import homePage.views

urlpatterns = [
    url(r'^$', homePage.views.redirectToHomePage),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^admin/', admin.site.urls),
    url(r'^home/', include('homePage.urls')),
    url(r'^search/', include('search.urls')),
    url(r'^course/', include('course.urls')),
    url(r'^operation/', include('databaseOperation.urls')),
    url(r'^user/', include('user.urls')),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^about/', homePage.views.about),
    url(r'^contactus/', homePage.views.contactUs),
]
