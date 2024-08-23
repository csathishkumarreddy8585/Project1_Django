from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse




def virat(request):
    return HttpResponse('virat is rcb captain')

def ABD(request):
    return render(request,'abd.html')