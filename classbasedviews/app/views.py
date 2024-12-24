from django.shortcuts import render
from django.views.generic import View
# Create your views here.

from django.http import HttpResponse

def String_fbv(request):
    return HttpResponse('<h1>string_fbv is doing</h1>')


class String_Cbv(View):
    def get(self,request):
        return HttpResponse('<h1>string_fbv is doing</h1>')



def html_fbv(request):
    return render (request,'html_fbv.html')

class html_Cbv(View):
    def get(self,request):
        return render(request,'html_cbv.html')