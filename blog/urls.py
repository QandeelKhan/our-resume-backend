# from django.urls import path, include
# from rest_framework.routers import DefaultRouter

# from .views import PostViewSet, CommentViewSet

# router = DefaultRouter()
# router.register(r'posts', PostViewSet, basename='post')
# router.register(r'comments', CommentViewSet, basename='comment')

# urlpatterns = [
#     path('', include(router.urls)),
# ]
from django.urls import path
from . import views

urlpatterns = [
    path('blogposts/', views.BlogPostList.as_view(), name='blogpost-list'),
    path('blogposts/<int:pk>/', views.BlogPostDetail.as_view(),
         name='blogpost-detail'),
    path('comments/', views.CommentList.as_view(), name='comment-list'),
    path('comments/<int:pk>/', views.CommentDetail.as_view(), name='comment-detail'),
    path('replies/', views.ReplyList.as_view(), name='reply-list'),
    path('replies/<int:pk>/', views.ReplyDetail.as_view(), name='reply-detail'),
]
