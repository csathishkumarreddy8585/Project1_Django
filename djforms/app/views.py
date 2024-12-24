from django.shortcuts import render

# Create your views here.

from app.forms import *

def insert_topic(request):
    SFO=topicsforms()
    d={'SFO':SFO}

    return render(request,'insert_topic.html',d)
