from django import forms


class topicsforms(forms.Form):
    topic_name=forms.CharField()