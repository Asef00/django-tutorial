from django.shortcuts import get_object_or_404, render
from django.http import Http404

# Create your views here.
from django.http import HttpResponse
from .models import Question
from .models import Quote

def index(request):
  latest_question_list = Question.objects.order_by("-pub_date")[:5]
  random_quote = Quote.objects.order_by('?').first()
  viewModel = {
    "latest_question_list": latest_question_list, 
    "quote_message": random_quote
  }
  return render(request, "polls/index.html", viewModel)

def detail(request, question_id):
  question = get_object_or_404(Question, pk=question_id)

  # try:
  #   question = Question.objects.get(pk=question_id)
  # except Question.DoesNotExist:
  #   raise Http404("Question does not exist")
  return render(request, "polls/details.html", {"question": question})

def results(request, question_id):
  response = "You're looking at the results of question %s."
  return HttpResponse(response % question_id)

def vote(request, question_id):
  return HttpResponse("You're voting on question %s." % question_id)