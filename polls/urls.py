"""
This module contains the URL configurations for your Django project.
"""

from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
]
