from django.urls import path, include
from rest_framework import routers
from .views import JobViewSet

router = routers.DefaultRouter()
router.register("", JobViewSet, basename="jobs")

app_name = "jobs"
urlpatterns = [path("", include(router.urls))]
