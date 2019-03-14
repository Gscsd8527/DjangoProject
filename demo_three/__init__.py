from __future__ import absolute_import

from .celery import app as celery_app
# 这是为了确保在django启动时启动 celery
