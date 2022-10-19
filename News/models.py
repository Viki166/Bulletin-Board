from tabnanny import verbose
from django.db import models
from Ads.models import Users



class Post(models.Model):
    header = models.CharField("Заголовок",max_length=255)
    text = models.TextField("Текст")
    datetime = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(Users,on_delete=models.CASCADE)
    category = models.ManyToManyField('Category',through='PostCategory')
    rating = models.IntegerField(default=0)
    
    def like(self):
        self.rating +=1
        self.save()

    def dislike(self):
        self.rating -=1
        self.save()
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural='Новости'


class Category(models.Model):
    name = models.CharField("Название", max_length=255)
    subscribers = models.ManyToManyField(Users, blank=True)
    
    def __str__(self):
        return f'{self.name}'
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural ='Категории'


class PostCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete= models.CASCADE)


class Response(models.Model):
    text = models.TextField("Текст")
    datetime = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(Users,on_delete=models.CASCADE)
    
    def like(self):
        self.rating +=1
        self.save()

    def dislike(self):
        self.rating -=1
        self.save()
    
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural='Комментарии'
