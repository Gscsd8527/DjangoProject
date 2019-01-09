from django.urls import path
from .views import *
from django.conf.urls import url
app_name = 'demo'
urlpatterns = [
    # path('index', index),
    url('^$', index),
    url(r'^(?P<id>\d+)$', show)
]