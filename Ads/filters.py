from tabnanny import verbose
from django_filters import FilterSet
from .models import Comment


class CommentsFilter(FilterSet):
    class Meta:
        model = Comment
        fields = {
            'ad': ['exact'],
        }
        