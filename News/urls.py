from django.urls import path
from .views import *



urlpatterns = [
path('', PostList.as_view(),name='posts'),
path('<int:pk>/', PostDetail.as_view(), name='post'),
path('create/', PostCreate.as_view(), name='create'),
path('update/', PostUpdate.as_view(), name='update'),
path('delete/', PostDelete.as_view(), name='delete'),
]
