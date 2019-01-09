from django.conf.urls import url
from test3.views import *
app_name = 'test3'
urlpatterns = [
    url(r'^index/$', index, name='index'),
    url(r'^myexp/$', MyExp, name='myexp'),
    url(r'^uploadPic/$', uploadPic, name='uploadPic'),
    url(r'^uploadHandle/$', uploadHandle, name='uploadHandle'),
    url(r'^herolist/(\d*)$', herolist, name='herolist'),
]