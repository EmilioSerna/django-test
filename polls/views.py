"""
This is the views.py file for the polls app.
"""
from django.http import HttpResponse


def index(request):
    """
    This is the index view for the polls app.
    """
    return HttpResponse("Hello, world. You're at the polls index.")


def detail(request, question_id):
    """
    This is the detail view for the polls app.
    """
    return HttpResponse(f"You're looking at question {question_id}.")


def results(request, question_id):
    """
    This is the results view for the polls app.
    """
    return HttpResponse(f"You're looking at the results of question {question_id}.")
