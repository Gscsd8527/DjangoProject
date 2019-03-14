from django.urls import path, include
from test4.views import *
from django.conf.urls import url
app_name = 'test4'
urlpatterns = [
   path('test/', test, name='test'),
   url('^fy/(\d+)/$', fenye, name='fy'),
   url('^ajaxstudents/$', ajaxstudents),
   url('^studentsinfo/$', studentsinfo),
   url('^celery/$', celery)
]
