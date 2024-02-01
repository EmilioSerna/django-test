"""
This module contains the Django models for the application.
"""
import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    """Question model for polls app"""

    def __str__(self):
        return str(self.question_text)

    def was_published_recently(self):
        """Check if the question was published recently.
        If the question was published within the last day, return True.

        :return: The result of the check.
        :rtype: bool
        """
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    """Choice model for polls app"""

    def __str__(self):
        return str(self.choice_text)

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
