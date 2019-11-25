from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import Selection, Participation, Choice


def index(request):
    # /selection/ GET -> 전체 selection 목록 보여주기
    latest_selection_list = Selection.objects.order_by('-pub_date')[:5]
    context = {
        'latest_selection_list': latest_selection_list,
    }
    # output = ', '.join([q.subject for q in latest_selection_list])
    return render(request, 'selection/index.html', context)


def detail(request, selection_id):
    # /selection/{selection_id} GET -> 특정 selection 정보 보여주기
    response = "You're looking at selection_id %s." % selection_id
    choice_list = Choice.objects.filter(selection_id=selection_id).order_by('-pub_date')
    context = {
        'choice_list': choice_list,
    }

    return render(request, 'selection/detail.html', context)

# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)
#
# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)
