from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import TweetSerializer, CustomUserSerializer, CommentSerializer
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

class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(tweet_id=self.kwargs['tweet_pk'])

    def get_serializer_context(self):
        return {'tweet_id': self.kwargs['tweet_pk']}
    
class CustomUserViewSet(CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated()]

    @action(detail=False, methods=['GET', 'PUT'])
    def me(self, request):
        (custom_user, created) = CustomUser.objects.get_or_create(user_id=request.user.id)
        if request.method == 'GET':
            serializer = CustomUserSerializer(custom_user)
            return Response(serializer.data)
        if request.method == 'PUT':
            serializer = CustomUserSerializer(custom_user, data=request.data)
            serializer.is_valid()
            serializer.save()
            return Response(serializer.data)