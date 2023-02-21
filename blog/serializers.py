
from rest_framework import serializers
from .models import BlogPost, BlogPostImage, Comment


class BlogPostImageSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = BlogPostImage
        fields = '__all__'

    def get_images(self, obj):
        if obj.images:
            return self.context['request'].build_absolute_uri(obj.images.url)
        return None


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


# class BlogPostSerializer(serializers.ModelSerializer):
#     comments = CommentSerializer(many=True, read_only=True)


class BlogPostSerializer(serializers.ModelSerializer):
    post_images = BlogPostImageSerializer(many=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = BlogPost
        fields = '__all__'
