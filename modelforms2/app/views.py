from django.shortcuts import render

# Create your views here.
from app.forms import *
from app.models import *

from django.http import HttpResponse


def Studentname(request):

    STFO=Studentforms()
    d={'STFO':STFO}

    if request.method=='POST':
        SDTFO=Studentforms(request.POST)
        if SDTFO.is_valid():
            SDTFO.save()
            return HttpResponse('Data is created')

        else: 
            return HttpResponse('Data is invalid')
    return render(request,'Studentname.html',d)








