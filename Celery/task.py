from celery import shared_task
import time
# celery -A djauth worker -l info -P eventletfor windows
# celery -A djauth worker -l info  for ubuntu 
@shared_task
def add(x, y):
    time.sleep(10)
    return x + y