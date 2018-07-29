from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^about', views.about, name='about'),
	url(r'^morearticles', views.morearticles, name='morearticles'),
	url(r'^login', views.login_user, name='login_user'),
	url(r'^logout', views.logout_user, name='logout_user'),
	url(r'^article/(?P<article_id>\d+)/$', views.article, name='article'),
	url(r'^article/add', views.addarticle, name='addarticle'),
	url(r'^article/edit/(?P<pk>[0-9]+)/$', views.editarticle.as_view(), name='editarticle'),
	url(r'^article/(?P<pk>[0-9]+)/delete/$', views.deletearticle, name='deletearticle'),
]