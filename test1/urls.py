from django.urls import path, include
from django.conf.urls import url
from test1.views import *
app_name = 'test1'
urlpatterns = [
    # url(r'')
    url(r'^(\d+)$', detail),
    # url(r'^(\d+)/(\d+)/(\d+)', index),  # 位置参数
    url(r'^(?P<p1>\d+)/(?P<p3>\d+)/(?P<p2>\d+)/', index),  # 关键字参数
    url(r'^getTest1/$', getTest1),
    url(r'^getTest2/$', getTest2),
    url(r'^getTest3/$', getTest3),

    url(r'^postTest1/$', postTest1),
    url(r'^postTest2/$', postTest2),

    url(r'^cookieTest/$', cookieTest),

    url(r'^redTest1/$', redTest1),
    url(r'^redTest2/$', redTest2, name='redTest2'),

    url(r'^session1/$', session1),
    url(r'^session2/$', session2),
    url(r'^session2_handle/$', session2_handle),
    url(r'^session3/$', session3),
]
