from rest_framework import viewsets
from .serializers import JobSerializer
from .models import Job


class JobViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = JobSerializer
    queryset = Job.objects.all()
