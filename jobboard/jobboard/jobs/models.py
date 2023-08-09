from django.db import models


class Job(models.Model):
    title = models.CharField(max_length=150)
    job_url = models.URLField()
    image_url = models.URLField("image")
    posted_at = models.DateTimeField()

    def __str__(self) -> str:
        return self.title
