from django.shortcuts import render

# Create your views here.
from app.forms import *
from app.models import *

from django.http import HttpResponse


def insert_topic(request):

    ETFO=topicforms()
    d={'ETFO':ETFO}

    if request.method=='POST':
        STFO=topicforms(request.POST)
        if STFO.is_valid():
            STFO.save()
            return HttpResponse('topic is valid')

        else: 
            return HttpResponse('topic is invalid')
    return render(request,'insert_webpages.html',d)




def insert_webpages(request):

    EWFO=Web_pagesfroms()
    d={'EWFO':EWFO}

    if request.method=='POST':
        STFO=Web_pagesfroms(request.POST)
        if STFO.is_valid():
            STFO.save()
            return HttpResponse('Webpages is inserted')
        else:
            return HttpResponse('webpages is invalid')
    return render(request,'insert_webpages.html',d)


    
def insert_AccessRecord(request):

    EAFO=Access_Recordfroms()
    d={'EAFO':EAFO}

    if request.method=='POST':
        STFO=Access_Recordfroms(request.POST)
        if STFO.is_valid():
            STFO.save()
            return HttpResponse('Access_Recordfroms is valid')
        else:
            return HttpResponse('Access_Recordfroms is invalid')
    return render(request,'insert_access.html',d)



def insert(request):
    
    ETFO=topicforms()
    EWFO=Web_pagesfroms()
    EAFO=Access_Recordfroms()
    d1={'ETFO':ETFO,'EWFO':EWFO,'EAFO':EAFO}
    
    

    if request.method=='POST':
        DTFO=topicforms(request.POST)
        
        if DTFO.is_valid():
            DTFO .save()
            return HttpResponse('is inserted')
        else:
            return HttpResponse(' is invalid')
    return render(request,'insert.html',d1)
    