from django.urls import path, include
from django.conf.urls import url
from test2.views import *
app_name = 'test2'
urlpatterns = [
   url(r'^index/$', index, name='index'),
   url(r'^(\d+)/$', show, name='show'),
   url(r'^index2/$', index2, name='index2'),
   url(r'^user1/$', user1, name='user1'),
   url(r'^user2/$', user2, name='user2'),
   url(r'^htmlTest/$', htmlTest, name='htmlTest'),
   url(r'^csrf1/$', csrf1, name='csrf1'),
]