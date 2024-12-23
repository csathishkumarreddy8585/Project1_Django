from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse


def studentdjf(request):

    ESFO=Student_detail()
    d={'ESFO':ESFO}

    if request.method=='POST':
        SFDO=Student_detail(request.POST)
        if SFDO.is_valid():
            
            return HttpResponse(' valid')
        else:
            return HttpResponse(' invalid')
    return render(request,'studentdjf.html',d)
