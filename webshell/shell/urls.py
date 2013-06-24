from django.conf.urls import patterns, include, url
from shell import views

urlpatterns = patterns('',
    url(r'^$', views.main, name='main'),
    url(r'^cd/(?P<dirname>.+?)$', views.cd, name='cd'),
    url(r'^cd/', views.cd, name='cd'),
    url(r'remove/file/(?P<filename>.+?)$', views.remove_file, name = 'remove_file'),
    url(r'remove/dir/(?P<dirname>.+?)$', views.remove_directory, name = 'remove_directory'),
    url(r'new/file/(?P<dirname>.+?)$', views.new_file, name = 'new_file'),
    url(r'new/directory/(?P<dirname>.+?)$', views.new_directory, name = 'new_directory'),
)