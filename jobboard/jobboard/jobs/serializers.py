from rest_framework import serializers
from .models import Job


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ("title", "image_url", "job_url", "posted_at")

    def to_representation(self, instance):
        instance.posted_at = instance.posted_at.strftime("%d %b, %Y")
        return super().to_representation(instance)
