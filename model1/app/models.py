from django.db import models

# Create your models here.
class deptno(models.Model):
    deptno=models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=100)
    dloc=models.CharField(max_length=100)

    def __str__(self):
        return self.dname +str(self.deptno)
class emp(models.Model):
    empno=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=100)
    job=models.CharField(max_length=100)
    hiredate=models.DateField()
    sal=models.DecimalField(max_digits=10,decimal_places=2)
    comm=models.DecimalField(max_digits=10,decimal_places=3,null=True,blank=True)
    mgr=models.ForeignKey('self',on_delete=models.SET_NULL,null=True,blank=True)
    deptno=models.ForeignKey(deptno,on_delete=models.CASCADE)

    def __str__(self):
        return self.ename

class salgrade(models.Model):
    grade=models.IntegerField(primary_key=True)
    losal=models.DecimalField(max_digits=10,decimal_places=4)
    hisal=models.DecimalField(max_digits=10,decimal_places=4)
    
    def __str__(self):
        return str(self.losal)


