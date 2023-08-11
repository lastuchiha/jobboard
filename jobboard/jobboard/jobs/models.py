from django.db import models


class Job(models.Model):
    class Meta:
        ordering = ["-posted_at"]

    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, db_index=True, max_length=150)
    job_url = models.URLField()
    image_url = models.URLField("image")
    posted_at = models.DateField()

    def __str__(self) -> str:
        return self.title
