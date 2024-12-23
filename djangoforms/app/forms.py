from django.shortcuts import render


from django import forms
def validate_char(data):
    if not data[0].isalpha():
        raise forms.ValidationError('invalid error')

# def validate_len(data):
#     if len(data)>5:
#         raise forms.ValidationError('invalid error')

class  Student_detail(forms.Form):
    sname=forms.CharField(validators=[validate_char])
    sid=forms.IntegerField()
    email=forms.EmailField()
    remail=forms.EmailField()
    url=forms.URLField()

