import os


def get_var(key):
    """Returns value of env var"""
    return os.getenv(key)
