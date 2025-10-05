from django import forms
from .models import *

class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogArticle
        fields = ["text"]
        labels = {"text":""}