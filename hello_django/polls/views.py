from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

def index(request):
  latest_question_list = Question.objects.order_by('-pub_date')[:5]
  context = {
    'latest_question_list': latest_question_list,
  }
  return HttpResponse(render(request, 'polls/index.html', context))

# Create your views here.

def detail(request, question_id):
  question_text = Question.objects.get(id=question_id).question_text
  output = f"You're looking at question {question_id}: {question_text}"
  return HttpResponse(output)

def results(request, question_id):
  response = "You're looking at the results of question %s."
  return HttpResponse(response % question_id)

def vote(request, question_id):
  return HttpResponse("You're voting on question %s." %question_id)
