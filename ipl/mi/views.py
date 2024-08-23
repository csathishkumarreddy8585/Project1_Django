from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse




def sky(request):
    return HttpResponse('sky india captain')

def hp(request):
    return render(request,'hp.html')