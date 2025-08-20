from rest_framework import serializers
from .models import Tweet, CustomUser

class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ['uuid', 'author', 'text', 'created_at']


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['uuid', 'username']

class CustomUserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['uuid', 'username', 'tweets']

    tweets = TweetSerializer(many=True, read_only=True)
