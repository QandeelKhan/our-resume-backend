
from rest_framework import serializers
from .models import BlogPost, BlogPostImage, Comment, Reply


class BlogPostImageSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = BlogPostImage
        fields = '__all__'

    def get_images(self, obj):
        if obj.images:
            return self.context['request'].build_absolute_uri(obj.images.url)
        return None


class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = '__all__'
        depth = 1

    def get_author_first_name(self, obj):
        return obj.author.first_name

    def get_author_last_name(self, obj):
        return obj.author.last_name


class CommentSerializer(serializers.ModelSerializer):
    replies = ReplySerializer(many=True, read_only=True)
    comment_count = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id', 'comment_count', 'replies', 'created_date',
                  'updated_at', 'comment_text', 'post', 'author']
        depth = 1

    def get_author_first_name(self, obj):
        return obj.author.first_name

    def get_author_last_name(self, obj):
        return obj.author.last_name

    def get_comment_count(self, obj):
        return obj.replies.count()

# class BlogPostSerializer(serializers.ModelSerializer):
#     post_images = BlogPostImageSerializer(many=True)
#     comments = CommentSerializer(many=True, read_only=True)

#     class Meta:
#         model = BlogPost
#         fields = '__all__'


class BlogPostSerializer(serializers.ModelSerializer):
    post_images = BlogPostImageSerializer(many=True)
    comments = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.SerializerMethodField()
    author_first_name = serializers.SerializerMethodField()
    author_last_name = serializers.SerializerMethodField()

    class Meta:
        model = BlogPost
        fields = [
            'id',
            'post_images',
            'comments',
            'comment_count',
            'title',
            'cover_image',
            'initial_paragraph',
            'paragraph_heading',
            'quote',
            'quote_writer',
            'second_paragraph',
            'paragraph_after_image',
            'author',
            'author_first_name',
            'author_last_name',
            'created_at',
            'updated_at',
            'category',
        ]
        depth = 1

    def get_author_first_name(self, obj):
        return obj.author.first_name

    def get_author_last_name(self, obj):
        return obj.author.last_name

    def get_comment_count(self, obj):
        return obj.comments.count()
