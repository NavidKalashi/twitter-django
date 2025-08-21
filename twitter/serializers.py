from rest_framework import serializers
from .models import Tweet, CustomUser, Comment

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

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'date', 'name', 'description']

    def create(self, validated_data):
        tweet_id = self.context['tweet_id']
        return Comment.objects.create(tweet_id=tweet_id, **validated_data)