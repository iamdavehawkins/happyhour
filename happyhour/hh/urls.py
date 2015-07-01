from django.conf.urls import url

from . import views

urlpatterns = [
	url('^$', views.now),
	url('^bar/(?P<rest_name>.+)/$', views.bar),
	url('^day/(?P<day>.+)/$', views.day)
]
