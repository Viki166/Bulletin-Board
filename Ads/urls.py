from django.urls import path
from .views import *


urlpatterns = [
    path('', AdsListView.as_view(), name='ads'),
    # path('celery-test/',index, name='celery_test_url'),
    path('<int:pk>/', DetailAd.as_view(), name='ad_detail'),
    path('comments/', Comments.as_view(), name = 'comments'),
    path('create/', AdCreate.as_view(), name='ad_create'),
    path('<int:pk>/update/', AdUpdateView.as_view(), name='ad_update'),
    path('<int:pk>/delete/', AdDeleteView.as_view(), name='ad_delete'),
    path('game/<str:game>/', GameList, name='game'),
    path('update_comment_active/<int:pk>/<slug:type>',updateCommentActive, name='update_comment_active'),
    path('comments/<int:pk>/like', AddCommentLike.as_view(), name = 'comment-like'),
    path('comments/<int:pk>/dislike', AddCommentDislike.as_view(), name = 'comment-dislike'),
   
    # path('login/', LoginView.as_view(template_name='sign/login.html'), name='login'),
    # path('logout/', LogoutView.as_view(template_name='sign/logout.html'), name='logout'),
]
 