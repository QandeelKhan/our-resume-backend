from django.contrib import admin
from .models import BlogPost, Category, Comment, Reply

# Register your models here.

from django import forms
# from django.contrib.admin.widgets import AdminFileWidget
from django.forms import ClearableFileInput

# to allow multiple images to upload in admin.py


class BlogPostAdminForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = '__all__'

    post_images = forms.FileField(
        widget=ClearableFileInput(attrs={'multiple': True}))


class BlogPostAdmin(admin.ModelAdmin):
    form = BlogPostAdminForm
    list_display = ['title', 'author', 'created_at', 'updated_at']
    search_fields = ['title', 'author']
    list_filter = ['created_at', 'updated_at']
    ordering = ['created_at']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name']
    ordering = ['category_name']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'author_name', 'created_date', 'updated_at']
    search_fields = ['post', 'author_name']
    list_filter = ['created_date', 'updated_at']
    ordering = ['created_date']


class ReplyAdmin(admin.ModelAdmin):
    list_display = ['comment', 'author', 'created_at', 'updated_at']
    search_fields = ['comment', 'author']
    list_filter = ['created_at', 'updated_at']
    ordering = ['created_at']


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Reply, ReplyAdmin)
