from django.conf.urls import patterns, include, url
from sitesearch import views

urlpatterns = patterns('',
                       url(r'^$', views.showform),
                       url(r'^add/$', views.add),
                       url(r'^(?P<site_id>\d+)/delete/$', views.delete),
                       )
