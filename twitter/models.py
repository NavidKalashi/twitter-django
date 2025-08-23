import uuid
from django.db import models
from django.conf import settings
from django.contrib import admin

class CustomUser(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    bio = models.TextField()
    birthday = models.DateField(null=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    
    @admin.display(ordering='user__username')
    def username(self):
        return self.user.username

    @admin.display(ordering='user__email')
    def email(self):
        return self.user.username
    
    class Meta:
        ordering = ['user__username']

class Tweet(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='tweets')

    def __str__(self) -> str:
        return self.author.username
    
    class Meta:
        ordering = ['created_at']

class Comment(models.Model):
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)