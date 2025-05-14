from django import forms

from app.models import *

class topicforms(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'



class Web_pagesfroms(forms.ModelForm):
    class Meta:
        model=Web_page
        fields='__all__'
        # fields=['topic_name','name']
        # exclude=['email','url']
        # labels={'topic_name':'TN'}
        # widgets={'url':forms.PasswordInput,'name':forms.Textarea}



class Access_Recordfroms(forms.ModelForm):
    class Meta:
        model=Access_Record
        fields='__all__'
        # fields=['name','Date']
        # exclude=['email']
        # labels={'topic_name':'TN'}

