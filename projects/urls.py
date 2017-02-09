from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.project_list, name='list'),
	url(r'^(?P<slug>[\w-]+)/$', views.project_detail, name='detail'),
]