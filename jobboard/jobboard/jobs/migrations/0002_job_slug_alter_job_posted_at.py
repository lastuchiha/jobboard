# Generated by Django 4.2.4 on 2023-08-10 03:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("jobs", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="job",
            name="slug",
            field=models.SlugField(default="test-slug", unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="job",
            name="posted_at",
            field=models.DateField(),
        ),
    ]
