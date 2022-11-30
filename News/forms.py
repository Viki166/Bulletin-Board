from django.forms import ModelForm
from django.forms import forms
from .models import News

class NewsForm(ModelForm):
    class Meta:
        model=News
        fields= ('header', 'text', 'image', 'category')