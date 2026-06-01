from django.contrib import admin
from .models import Post, Comment
# Register your models here.
@admin.register(Post)
class Post(admin.ModelAdmin):
  list_display = ['id', 'title', 'content', 'status']
  list_filter = ['status']
  search_fields = ['title', 'content']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
  list_display = ['id', 'author', 'post', 'content', 'parent']