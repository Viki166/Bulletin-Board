from django.db import models
from django.contrib.auth.models import User
from Ads.models import Users

class News(models.Model):
    header = models.CharField(max_length=255)
    text = models.TextField()
    image = models.ImageField(height_field=225, width_field=400,upload_to='MEDIA_ROOT')
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    date =models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField('Category', through='NewsCategory')
    like = models.ManyToManyField(Users, blank=True, related_name ='news_like')
    dislike = models.ManyToManyField(Users, blank=True, related_name='news_dislike')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Category(models.Model):
    name = models.CharField(max_length=255) 
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class NewsComment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    like = models.ManyToManyField(Users, blank=True, related_name ='comment_like')
    dislike = models.ManyToManyField(Users, blank=True, related_name='comment_dislike')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

class NewsCategory(models.Model):
    news = models.ForeignKey(News,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)