from demo_three import celery_app
from celery import shared_task
from time import sleep


@celery_app.task()
def UploadTask(message):
    UploadTask.update_state(state='PROGRESS', meta={'progress': 0})
    sleep(30)
    UploadTask.update_state(state='PROGRESS', meta={'progress': 30})
    sleep(30)
    return message


def get_task_status(task_id):
    task = UploadTask.AsyncResult(task_id)

    status = task.state
    progress = 0

    if status == u'SUCCESS':
        progress = 100
    elif status == u'FAILURE':
        progress = 0
    elif status == 'PROGRESS':
        progress = task.info['progress']

    return {'status': status, 'progress': progress}


@celery_app.task
def add(x, y):
    return x + y


def mul(x, y):
    return x * y