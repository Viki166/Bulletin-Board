from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField



class Users(models.Model):
    user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Game(models.Model):
    name = models.CharField("Название", max_length=225)
    
    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'

class Ad(models.Model):
    header = models.CharField("Заголовок", max_length=225)
    content_upload = RichTextUploadingField("Текстовое поле", blank=True, null=True)
    datetime = models.DateTimeField("Дата и время", auto_now_add=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    game = models.ForeignKey('Game', on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.user}'
    
    
    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def get_absolute_url(self):
        return f'/{self.id}'


class Category(models.Model):
    name = models.CharField("Категория", max_length=225)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Response(models.Model):
    text = models.TextField("Текст")
    datetime = models.DateTimeField("Дата и время", auto_now_add=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    ad = models.ForeignKey('Ad', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Отклик'
        verbose_name_plural = 'Отклики'

