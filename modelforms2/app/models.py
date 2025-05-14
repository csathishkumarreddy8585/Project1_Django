from django.db import models

# Create your models here.

from django.core import validators

from django.core.validators import *


class Student(models.Model):
    Sname=models.CharField(max_length=100,primary_key=True)
    Sid=models.IntegerField()
    Semail=models.EmailField()
   
    url=models.URLField()
    phone=models.CharField(max_length=10,validators=[validators.RegexValidator('[6-9] \d { 9}')])
    

    def __str__(self):
        return self.Sname


