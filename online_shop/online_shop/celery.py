import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'online_shop.settings')

app = Celery('online_shop')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()