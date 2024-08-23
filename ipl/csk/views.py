from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def msd(request):
    return HttpResponse('msd is cool captain')


def RJ(request):
    return HttpResponse('RJ is csk captain')