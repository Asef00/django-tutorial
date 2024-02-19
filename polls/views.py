from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Question
from .models import Quote

def index(request):
  latest_question_list = Question.objects.order_by("-pub_date")[:5]
  random_quote = Quote.objects.get(id=1)
  viewModel = {
    "latest_question_list": latest_question_list, 
    "quote_message": random_quote
  }
  return render(request, "polls/index.html", viewModel)

def detail(request, question_id):
  return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
  response = "You're looking at the results of question %s."
  return HttpResponse(response % question_id)

def vote(request, question_id):
  return HttpResponse("You're voting on question %s." % question_id)