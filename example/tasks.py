
from celery import shared_task
from time import sleep 

@shared_task
def do_some_expensive_things(duration):
    sleep(duration)
    return "Done"