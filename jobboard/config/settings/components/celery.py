from celery.beat import crontab

CELERY_BROKER_URL = "redis://localhost:6379/0"
CELERY_RESULT_BACKEND = "redis://localhost:6379/1"

CELERY_BEAT_SCHEDULE = {
    "my-scheduled-task": {
        "task": "jobboard.jobs.tasks.scraper_task",
        "schedule": crontab(hour=18, minute=15),
    }
}
