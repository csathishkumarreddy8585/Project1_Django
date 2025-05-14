from django.shortcuts import render
from django.db.models import Avg,Sum,Max,Min,Count
# Create your views here.

from app.models import *

def empdept(request):
    edos=emp.objects.all()
    d={'edos':edos}
    return render(request,'empdept.html',d)

def empdept(request):

    emp.objects.filter(ename='sathish').update(job='html')
    emp.objects.filter(empno=7).update(hiredate='2024-5-25')
    emp.objects.filter(comm=50000).update(sal='80000')
    emp.objects.filter(comm=50000).update(ename='account')
    edos=emp.objects.select_related('deptno')
    d={'edos':edos}
    return render(request,'empdept.html',d)

def empmgr(request):
     emos=emp.objects.select_related('mgr').all()
     emos=emp.objects.select_related('mgr').filter(mgr__sal__gt=20000)
     emos=emp.objects.select_related('mgr').filter(mgr__sal__lt=20000)
     emos=emp.objects.select_related('deptno','mgr').filter(mgr__isnull=False)
     print(emp.objects.values(deptno).annotate(Avg('sal')))
     print(emp.objects.filter(deptno=8).aggregate(Avg('sal')))
     d={'emos':emos}
     return render(request,'empmgr.html',d)

def empdeptmgr(request):
    edmos=emp.objects.select_related('deptno').all()
    edmos=emp.objects.select_related('deptno','mgr').filter(mgr__sal__gt=20000)
    edmos=emp.objects.select_related('deptno','mgr').filter(mgr__sal__lt=20000)
    edmos=emp.objects.select_related('deptno','mgr').filter(mgr__isnull=False)
   
    d={'edmos':edmos}
    print(emp.objects.values(deptno).annotate(Avg('sal')))
    print(emp.objects.filter(deptno=8).aggregate(Avg('sal')))
    print()

    return render(request,'empdeptmgr.html',d)

def deptemp(request):
    deptno.objects.filter(dname='shiva').update(dloc='b.k')
    DEO=deptno.objects.prefetch_related('emp_set').all()
    d={'DEO':DEO}
    return render(request,'deptemp.html',d)




