from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^register/$', views.register, name='register'),
	url(r'^login/$', views.user_login, name='user_login'),
	url(r'^logout/$', views.user_logout, name='user_logout'),
	url(r'^add_hh/$', views.add_hh, name='add_hh'),
	url(r'^$', views.index),
	url(r'^bar/(?P<rest_name>.+)/$', views.bar),
	url(r'^day/(?P<day>.+)/$', views.day)
]
