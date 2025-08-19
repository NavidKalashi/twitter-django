from django.contrib import admin
from . import models

@admin.register(models.Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ['author', 'text']
    list_per_page = 5

@admin.register(models.CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'bio']
    list_per_page = 10