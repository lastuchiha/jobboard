# Generated by Django 4.2.4 on 2023-08-08 13:28

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Job",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=150)),
                ("job_url", models.URLField()),
                ("image_url", models.URLField(verbose_name="image")),
                ("posted_at", models.DateTimeField()),
            ],
        ),
    ]
