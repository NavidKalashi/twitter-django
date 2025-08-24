from rest_framework import serializers
from .models import Tweet, CustomUser, Comment

class TweetSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source="author.user.username", read_only=True)
    
    class Meta:
        model = Tweet
        fields = ['uuid', 'author', 'text', 'created_at']

class CustomUserSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = CustomUser
        fields = ['uuid', 'user_id', 'bio', 'birthday']

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