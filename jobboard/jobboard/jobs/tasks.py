from celery import shared_task

# from jobboard.scraper import scrapper


@shared_task
def scraper_task():
    print("Hurray")
