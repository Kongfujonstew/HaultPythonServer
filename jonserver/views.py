# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render

from django.http import HttpResponseRedirect, HttpResponse

from django.urls import reverse

from django.http import Http404

from django.views import generic

from django.utils import timezone

from django.template import loader

from .models import Choice, Question, Pageviews
# , Profiles, Pageviews


class IndexView(generic.ListView):
    template_name = 'jonserver/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(
          pub_date__lte=timezone.now()
          ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'jonserver/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'jonserver/results.html'


def vote(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  try:
    selected_choice = question.choice_set.get(pk=request.POST['choice'])
  except (KeyError, Choice.DoesNotExist):
    return render(request, 'jonserver/detail.html', {
      'question': question,
      'error_message': "You didn't select a choice",
      })
  else:
    selected_choice.votes += 1
    selected_choice.save()
    return HttpResponseRedirect(reverse('jonserver:results', args=(question.id,)))

def add_pageview(request):
    print 'addpageview received'
    newpv = Pageviews(
      profile_id=99999,
      url="www.fakeurl.com", 
      title="fake site4testo",
      time_open=timezone.now(),
      # time_closed= ???
      is_active=False
      )
    newpv.save()

    return HttpResponse('saved')

def hello(request):
  return HttpResponse('hello dere')


getAll, getActive, search, visitPage, deactivatePage, deletePage,


# def index(request):
#   latest_question_list = Question.objects.order_by('-pub_date')[:5]
#   template = loader.get_template('jonserver/index.html')
#   context = {
#     'latest_question_list': latest_question_list,
#   }
#   # output = ', '.join([q.question_text for q in latest_question_list])
#   return render(request, 'jonserver/index.html', context)

# def detail(request, question_id):
#   print 'success endpoint hit question_id or pk = ', question_id
#   question = get_object_or_404(Question, pk=question_id)
#   return render(request, 'jonserver/detail.html', {'question': question})

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'jonserver/results.html', {'question': question})

# def vote(request, question_id):
#   question = get_object_or_404(Question, pk=question_id)
#   try:
#     selected_choice = question.choice_set.get(pk=request.POST['choice'])
#   except (KeyError, Choice.DoesNotExist):
#     return render(request, 'jonserver/detail.html', {
#       'question': question,
#       'error_message': "You didn't select a choice",
#       })
#   else:
#     selected_choice.votes += 1
#     selected_choice.save()
#     return HttpResponseRedirect(reverse('jonserver:results', args=(question.id,)))

# def hello(request):
#   return HttpResponse('hello dere')

