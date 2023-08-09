from utils.get_env_or_exception import get_env_or_exception

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "jobboard",
        "USER": "postgres",
        "PASSWORD": get_env_or_exception("POSTGRES_PASSWORD"),
        "HOST": "localhost",
        "PORT": "5432",
    }
}
