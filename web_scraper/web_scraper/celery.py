from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings


# setting the Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_scraper.settings')
app = Celery('web_scraper')
app.config_from_object('django.conf:settings', namespace='CELERY')

# Looks up for task modules in Django applications and loads them
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
