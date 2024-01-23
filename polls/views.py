"""
This is the views.py file for the polls app.
"""
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Question


def index(request):
    """
    This is the index view for the polls app.
    """
    context = {
        "latest_question_list": Question.objects.order_by("-pub_date")[:5],
    }
    return render(request, "polls/index.html", context)


def detail(request, question_id):  # pylint: disable=unused-argument
    """
    This is the detail view for the polls app.
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):  # pylint: disable=unused-argument
    """
    This is the results view for the polls app.
    """
    return HttpResponse(f"You're looking at the results of question {question_id}.")


def vote(request, question_id):  # pylint: disable=unused-argument
    """
    This is the vote view for the polls app.
    """
    return HttpResponse(f"You're voting on question {question_id}.")
