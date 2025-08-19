import uuid
from django.db import models

class CustomUser(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    bio = models.TextField()
    birthday = models.DateField(null=True)

    def __str__(self) -> str:
        return self.username
    
    class Meta:
        ordering = ['username']

class Tweet(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.author.username
    
    class Meta:
        ordering = ['created_at']