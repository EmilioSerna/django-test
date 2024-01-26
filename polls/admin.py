"""This file is used to register the Question model with the admin site."""
from django.contrib import admin

from .models import Question, Choice

admin.site.register(Question)
admin.site.register(Choice)
