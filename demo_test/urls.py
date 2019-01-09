from django.conf.urls import url
from demo_test.views import *
from django.urls import path
app_name = 'demo_test'
# app_name = 'demo_test'
urlpatterns = [
    url('^$', index),
]