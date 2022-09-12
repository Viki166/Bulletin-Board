from django.urls import path
from .views import *


urlpatterns = [
    path('ads/', AdsListView.as_view(), name='ads'),
    path('ads/<int:pk>/', DetailAd.as_view(), name='ad_detail'),
    path('ads/comments/', Comments.as_view(), name = 'comments'),
    path('ads/create/', AdCreate.as_view(), name='ad_create'),
    path('ads/<int:pk>/update/', AdUpdateView.as_view(), name='ad_update'),
    path('ads/<int:pk>/delete/', AdDeleteView.as_view(), name='ad_delete'),
    path('ads/game/<str:game>/', GameList, name='game'),
    # path('login/', LoginView.as_view(template_name='sign/login.html'), name='login'),
    # path('logout/', LogoutView.as_view(template_name='sign/logout.html'), name='logout'),
]
