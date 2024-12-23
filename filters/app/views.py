from django.shortcuts import render

# Create your views here.

def filter(request):
    import datetime
    dt=datetime.datetime.now()
    d={'DTO':'SAthIsh kUmAr rEdDy','dt':dt,'c':1}
    return render(request,'filter.html',d)


def myfilter(request):
    d={'FTO':'Today is sunday'}
    return render(request,'myfilter.html',d)
