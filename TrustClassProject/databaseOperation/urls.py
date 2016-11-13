from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'create/createcourse$', views.createCourse),
    url(r'create/course$', views.createCoursePage),
	url(r'create/review$', views.createCourseReview),
    url(r'edit/course/(?P<courseID>[0-9]+)$', views.editCoursePage),
    url(r'edit/editcourse$', views.editCourse),
    url(r'refresh/captcha$', views.ajaxNewCaptcha),
    url(r'add/likecount$', views.ajaxLike),
    url(r'add/dislikecount$', views.ajaxDislike),
    url(r'add/collect$', views.ajaxCollect),
]
