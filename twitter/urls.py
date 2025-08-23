from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('tweets', views.TweetViewSet)
router.register('custom-users', views.CustomUserViewSet)

tweet_router = routers.NestedDefaultRouter(router, 'tweets', lookup='tweet')
tweet_router.register('comments', views.CommentViewSet, basename='tweet-comments')

urlpatterns = router.urls + tweet_router.urls
