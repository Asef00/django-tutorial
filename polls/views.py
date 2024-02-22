from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.db.models import F
from django.views import generic

# Create your views here.
from .models import Question
from .models import Quote
from .models import Choice

class IndexView(generic.ListView):
  template_name = "polls/index.html"
  context_object_name = "latest_question_list"

  def get_queryset(self):
    return Question.objects.order_by("-pub_date")[:5]
  
class DetailView(generic.DetailView):
  model = Question
  template_name = "polls/details.html"

class ResultsView(generic.DetailView):
  model = Question
  template_name = "polls/results.html"

# def index(request):
#   latest_question_list = Question.objects.order_by("-pub_date")[:5]
#   random_quote = Quote.objects.order_by('?').first()
#   viewModel = {
#     "latest_question_list": latest_question_list, 
#     "quote_message": random_quote
#   }
#   return render(request, "polls/index.html", viewModel)

# def detail(request, question_id):
#   question = get_object_or_404(Question, pk=question_id)

#   # try:
#   #   question = Question.objects.get(pk=question_id)
#   # except Question.DoesNotExist:
#   #   raise Http404("Question does not exist")
#   return render(request, "polls/details.html", {"question": question})

# def results(request, question_id):
#   question = get_object_or_404(Question, pk=question_id)
#   return render(request, "polls/results.html", {"question": question})

def vote(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  try:
    selected_choice = question.choice_set.get(pk=request.POST["choice"])
  except (KeyError, Choice.DoesNotExist):
    return render(
      request,
      "polls/details.html",
      {
        question: question,
        "error_message": "You didn't select a choice.",
      },
    )
  else:
    selected_choice.votes = F("votes") + 1
    selected_choice.save()

    return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))