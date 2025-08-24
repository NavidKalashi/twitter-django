from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly
from .serializers import TweetSerializer, CustomUserSerializer, CommentSerializer, CustomUserDetailSerializer
from .models import Tweet, CustomUser, Comment
from .pagination import DefaultPagination
from .permissions import IsAdminOrAuthenticated

class TweetViewSet(ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    pagination_class = DefaultPagination
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    search_fields = ['text']
    ordering_fields = ['created_at']

    def get_serializer_context(self):
        return {'request': self.request}
    
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
        
    @action(detail=False, methods=['GET', 'PUT', 'DELETE'], permission_classes=[IsAuthenticated])
    def me(self, request):
        custom_user = get_object_or_404(CustomUser, user=request.user)

        if request.method == 'GET':
            tweet = get_object_or_404(Tweet, author=custom_user)
            serializer = TweetSerializer(tweet, context={'request': request})
            return Response(serializer.data)

        if request.method == 'PUT':
            tweet, created = Tweet.objects.get_or_create(author=custom_user)
            serializer = TweetSerializer(tweet, data=request.data, partial=True, context={'request': request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)

        if request.method == 'DELETE':
            tweet = get_object_or_404(Tweet, author=custom_user)
            tweet.delete()
            return Response({"detail": "Tweet deleted successfully."}, status=204)

class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(tweet_id=self.kwargs['tweet_pk'])

    def get_serializer_context(self):
        return {'tweet_id': self.kwargs['tweet_pk']}
    
class CustomUserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    # def get_permissions(self):
    #     if self.request.method == 'GET':
    #         return [AllowAny()]
    #     return [IsAdminUser()]

    @action(detail=False, methods=['GET', 'PUT'], permission_classes=[IsAuthenticated])
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