from django.conf.urls.defaults import *
from django.conf import settings
from core import views

media_root = settings.MEDIA_ROOT

urlpatterns = patterns('',url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':media_root}),)

urlpatterns += patterns(
    '',
    url(r'^$', views.home, {}, name='home'),
    url(r'^article/create/$', views.create_article, name='create_article'),
    url(r'^article/(?P<article_id>\d+)/$', views.read_article, name='read_article'),
    url(r'^article/edit/(?P<article_id>\d+)/$', views.update_article, name='update_article'),
    url(r'^article/(?P<article_id>\d+)/delete/$', views.delete_article, name='delete_article'),
)

if settings.DEBUG:
    urlpatterns += patterns(
        '',
        url(r'^500/$', 'django.views.generic.simple.direct_to_template', {'template': '500.html'}),
        url(r'^404/$', 'django.views.generic.simple.direct_to_template', {'template': '404.html'}),
        )
