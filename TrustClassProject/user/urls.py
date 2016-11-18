from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'login/$', views.loginPage),
	url(r'login/action$', views.loginAction),
	url(r'signup/$', views.signUpPage),
	url(r'signup/action$', views.signUp),
	url(r'logout/action$', views.logoutAction),
	url(r'changefollowstatus/action$', views.ajaxChangeFollowStatus),
	url(r'follow/', views.followListPage),
	url(r'collection/p(?P<page>[0-9]+)', views.collectionPage),
	url(r'collection/', views.redirectToCollectionPage),
	url(r'^profile/$', views.profilePage),
        url(r'^api/profile/(?P<pk>[0-9]*)$', views.api_TCUserProfile.as_view()),
]
