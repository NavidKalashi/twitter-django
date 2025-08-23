from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import TweetSerializer, CustomUserSerializer, CustomUserDetailSerializer, CommentSerializer
from .models import Tweet, CustomUser, Comment
from .pagination import DefaultPagination

class TweetViewSet(ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    pagination_class = DefaultPagination
    search_fields = ['text']
    ordering_fields = ['created_at']

    def get_serializer_context(self):
        return {'request': self.request}
    
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

# class CustomUserList(ListCreateAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = CustomUserSerializer

#     def get_serializer_context(self):
#         return {'request': self.request}

# class CustomUserDetail(APIView):
#     def get(self, request, pk):
#         customuser = get_object_or_404(CustomUser, pk=pk)
#         serializer = CustomUserDetailSerializer(customuser, context={'request': request})
#         return Response(serializer.data)
    
class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(tweet_id=self.kwargs['tweet_pk'])

    def get_serializer_context(self):
        return {'tweet_id': self.kwargs['tweet_pk']}