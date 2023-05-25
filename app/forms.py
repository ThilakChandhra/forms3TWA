from django import forms
from app.models import *

class topic(forms.Form):
    topic_name=forms.CharField(max_length=100)

class webpage(forms.Form):
    topic_name=forms.CharField(max_length=100)
    name=forms.CharField(max_length=100)
    email=forms.EmailField()
    url=forms.URLField()

class access(forms.Form):
    name=forms.CharField(max_length=100)
    author=forms.CharField(max_length=100)
    date=forms.DateField()
    