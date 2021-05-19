import os
import time

from celery import Celery


celery = Celery(__name__)
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL", "redis://127.0.0.1:6379")
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND", "redis://127.0.0.1:6379")


@celery.task(name="create_task")
def create_task(task_type):
    try:
        time.sleep(int(task_type) * 10)
        return True
    except (ValueError, TypeError):
        return False

