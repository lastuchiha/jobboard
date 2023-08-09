import os
from celery import Celery

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    f"jobboard.settings.{os.environ.get('DJANGO_ENV', 'dev')}",
)

app = Celery("jobboard")
app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()
