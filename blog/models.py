from django.db import models
from UserManagement.models import User
from django.core.files.storage import FileSystemStorage
from PIL import Image


# make custom storage backend for image
fs = FileSystemStorage(location='/media/images/')


def validate_image(image):
    try:
        img = Image.open(image)
        img.verify()
    except (IOError, SyntaxError) as e:
        raise ValidationError("Invalid image: %s" % e)


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    # applying custom storage backend
    cover_image = models.ImageField(upload_to='blog-images/',
                                    storage=fs, validators=[validate_image])
    initial_paragraph = models.TextField()
    paragraph_heading = models.CharField(max_length=255)
    quote = models.CharField(max_length=255)
    quote_writer = models.CharField(max_length=255)
    second_paragraph = models.TextField()
    post_images = models.ImageField(upload_to='blog-images/',
                                    storage=fs, validators=[validate_image])
    paragraph_after_image = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        BlogPost, on_delete=models.CASCADE, related_name='comments')
    author_name = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    comment_text = models.TextField()

    def __str__(self):
        return self.comment_text
