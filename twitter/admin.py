from django.contrib import admin
from . import models

@admin.register(models.Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ['short_text']
    list_per_page = 10
    list_select_related = ['author']
    list_filter = ['updated_at']

    def short_text(self, tweet):
        return (tweet.text[:50] + '...    |  ' + tweet.author.username if len(tweet.text) > 50 else tweet.text)
    
    short_text.short_description = "text"

@admin.register(models.CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'bio']
    list_per_page = 10
    search_fields = ['username__istartswith']