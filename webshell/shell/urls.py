from django.conf.urls import patterns, include, url
from shell import views

urlpatterns = patterns('',
    url(r'^$', views.main, name='main'),
    url(r'^cd/(?P<dirname>.+?)$', views.cd, name='cd'),
    url(r'^cd/', views.cd, name='cd'),
    url(r'remove/(?P<filename>.+?)$', views.remove, name = 'remove'),
    url(r'new/file/(?P<dirname>.+?)$', views.new_file, name = 'new_file'),
    url(r'new/directory/(?P<dirname>.+?)$', views.new_directory, name = 'new_directory'),
    url(r'uplink/(?P<dirname>.+?)$', views.uplink, name='uplink'),
)