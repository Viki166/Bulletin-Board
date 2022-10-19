from django.contrib import admin
from .models import Post, Category, Response


# class PostAdmin(admin.ModelAdmin):
#     list_display = ['id','header','datetime','category']
#     list_display_links = ['id','header']
#     search_fields = ['header','text']



admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Response)