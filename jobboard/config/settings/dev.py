from .base import *
from .components.postgres import *
from .components.celery import *
from .components.restframework import *

DEBUG = True

CORS_ALLOWED_ORIGINS = ["http://localhost:5137"]
