from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from .serializers import TweetSerializer, CustomUserSerializer, CustomUserDetailSerializer
from .models import Tweet, CustomUser

class TweetList(ListCreateAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer

    def get_serializer_context(self):
        return {'request': self.request}

class TweetDetail(RetrieveUpdateDestroyAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    
    def delete(self, request, pk):
        tweet = get_object_or_404(Tweet, pk=pk)
        tweet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CustomUserList(ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def get_serializer_context(self):
        return {'request': self.request}

class CustomUserDetail(APIView):
    def get(self, request, pk):
        customuser = get_object_or_404(CustomUser, pk=pk)
        serializer = CustomUserDetailSerializer(customuser, context={'request': request})
        return Response(serializer.data)