from .models import Ad, Comment
from django.forms import ModelForm, Textarea, Select
from django import forms
class AdForm(ModelForm):
    class Meta:
        model = Ad
        fields = ('header', 'content_upload', 'user', 'category','game')
       

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields= ('text',)

        widgets = {
            'text': forms.Textarea( attrs = {'rows':5, 'placeholder':'Комментарий'}),
        }