"""
This file is used to configure the polls app.
"""
from django.apps import AppConfig


class PollsConfig(AppConfig):
    """
    This class is used to configure the polls app.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "polls"
