from django import forms

from app.models import *

class Studentforms(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'

    Remail=forms.EmailField()



