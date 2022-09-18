from gc import get_objects
from multiprocessing import context
from webbrowser import get
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import *
# Create your views here.

def boards(request):
    boards=Board.objects.all()
    context={'boards':boards}
    return render(request,'home.html',context)


def board_topics(request,board_id):
    board=Board.objects.get(pk=board_id)
    # board=get_object_or_404(Board,pk=board_id)
    return render(request,'topic.html',{'board':board})
