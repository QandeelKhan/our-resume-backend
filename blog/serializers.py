
from rest_framework import serializers
from .models import BlogPost, BlogPostImage


class BlogPostImageSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = BlogPostImage
        fields = '__all__'

    def get_images(self, obj):
        if obj.images:
            return self.context['request'].build_absolute_uri(obj.images.url)
        return None


class BlogPostSerializer(serializers.ModelSerializer):
    post_images = BlogPostImageSerializer(many=True)

    class Meta:
        model = BlogPost
        fields = '__all__'
