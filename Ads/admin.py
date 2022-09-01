from django.contrib import admin
from .models import Users, Game, Ad, Category, Comment



class AdAdmin(admin.ModelAdmin):
    list_display = ('id','header','datetime','user', 'category','game')
    list_display_links = ('id','header')
    search_fields=('header','text')




admin.site.register(Users)
admin.site.register(Game)
admin.site.register(Ad, AdAdmin)
admin.site.register(Category)
admin.site.register(Comment)
