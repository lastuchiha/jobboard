from celery import shared_task
from jobboard.scraper import jobscraper


@shared_task
def scraper_task():
    print("Hurray")
