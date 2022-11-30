from django.contrib import admin
from .models import News, Category, NewsComment

admin.site.register(News)
admin.site.register(Category)
admin.site.register(NewsComment)