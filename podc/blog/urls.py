from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^about', views.about, name='about'),
	url(r'^login', views.login, name='login'),
	url(r'^article/(?P<article_id>\d+)/$', views.article, name='article'),
	url(r'^article/add', views.addarticle, name='addarticle'),
]