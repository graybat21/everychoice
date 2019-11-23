from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from .models import Selection


def index(request):
    # /selection/ GET -> 전체 selection 목록 보여주기
    # return HttpResponse("Hello, world. You're at the polls index.")
    latest_selection_list = Selection.objects.order_by('-pub_date')[:5]
    template = loader.get_template('selection/index.html')
    context = {
        'latest_selection_list': latest_selection_list,
    }
    # output = ', '.join([q.subject for q in latest_selection_list])
    return HttpResponse(template.render(context, request))

def detail(request, selection_id):
    # /selection/{selection_id} GET -> 특정 selection 정보 보여주기
    return HttpResponse("You're looking at question %s." % selection_id)

# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)
#
# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)