import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_example.settings')

app = Celery('celery_example')
# app.conf.broker_url = 'redis://localhost:6379/0'
print("celery app", app)
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')