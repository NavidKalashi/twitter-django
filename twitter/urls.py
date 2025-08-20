from django.urls import path
from . import views

urlpatterns = [
    path('tweets/', views.TweetList.as_view()),
    path('tweets/<uuid:pk>/', views.TweetDetail.as_view()),
    path('users/', views.CustomUserList.as_view()),
    path('users/<uuid:pk>/', views.CustomUserDetail.as_view(), name='custom-user-detail'),
]
