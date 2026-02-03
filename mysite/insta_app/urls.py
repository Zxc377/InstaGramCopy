from django.urls import path, include
from rest_framework import routers
from .views import (UserProfileViewSet, FollowViewSet, RegionViewSet,
                    HashtagViewSet, PostListAPIView, ContentViewSet, PostLikeViewSet,
                    PostDetailAPIView,CommentViewSet, CommentLikeViewSet)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



router = routers.DefaultRouter()
router.register('users', UserProfileViewSet)
router.register('follows', FollowViewSet)
router.register('regions', RegionViewSet)
router.register('hashtags', HashtagViewSet)
router.register('contents', ContentViewSet)
router.register('likes', PostLikeViewSet)
router.register('comments', CommentViewSet)
router.register('comment-likes', CommentLikeViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('post/', PostListAPIView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailAPIView.as_view(), name='post-detail'),

]
