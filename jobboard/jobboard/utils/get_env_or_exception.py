import os
from django.core.exceptions import ImproperlyConfigured


def get_env_or_exception(var_name):
    """
    Return environment variable if exists otherwise returns an Exception
    """
    try:
        return os.environ[var_name]
    except KeyError:
        err_msg = "Set the {0} environment variable".format(var_name)
        raise ImproperlyConfigured(err_msg)
