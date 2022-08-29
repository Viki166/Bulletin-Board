from pyexpat import model
from .models import Ad,Response
from django.forms import ModelForm


class AdForm(ModelForm):
    class Meta:
        model = Ad
        fields = ('header', 'content_upload', 'user', 'category','game')
       

class ResponseForm(ModelForm):
    model = Response
    fields= ('__all__')
