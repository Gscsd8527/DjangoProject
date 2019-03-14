from __future__ import absolute_import

from celery import Celery
from django.conf import settings
import os

#设置环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo_three.settings')

#实例化Celery
app = Celery('demo_three')

#使用django的settings文件配置celery
app.config_from_object('django.conf:settings')
#Celery加载所有注册的应用
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
