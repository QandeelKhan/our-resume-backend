from rest_framework import viewsets


# class BlogPostViewSet(viewsets.ModelViewSet):
#     queryset = BlogPost.objects.all()
#     serializer_class = BlogPostSerializer


# class CommentViewSet(viewsets.ModelViewSet):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer


# router = routers.DefaultRouter()
# router.register(r'blog-posts', BlogPostViewSet)
# router.register(r'comments', CommentViewSet)


# class BlogPostViewSet(viewsets.ModelViewSet):
#     queryset = BlogPost.objects.all()
#     serializer_class = BlogPostSerializer

#     def get_queryset(self):
#         if self.request.user.is_superuser or self.request.user.is_staff:
#             return BlogPost.objects.all()
#         return BlogPost.objects.none()

#     def perform_create(self, serializer):
#         if self.request.user.is_superuser or self.request.user.is_staff:
#             serializer.save(author=self.request.user)


# from rest_framework import viewsets
# from rest_framework.permissions import IsAdminUser, IsAuthenticated

# from .models import Post, Comment
# from .serializers import PostSerializer, CommentSerializer

# class PostViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     permission_classes = [IsAdminUser | IsAuthenticated]

# class CommentViewSet(viewsets.ModelViewSet):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     permission_classes = [IsAuthenticated]
from rest_framework import generics
from .models import BlogPost, Comment, Reply
from .serializers import BlogPostSerializer, CommentSerializer, ReplySerializer


class BlogPostList(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer


class BlogPostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class ReplyList(generics.ListCreateAPIView):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer


class ReplyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer
