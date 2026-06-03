from django.contrib import admin
from .models import Post, Comment, PostLike, CommentLike, Bookmark
# Register your models here.
@admin.register(Post)
class Post(admin.ModelAdmin):
  list_display = ['id', 'title', 'content', 'status']
  list_filter = ['status']
  search_fields = ['title', 'content']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
  list_display = ['id', 'author', 'post', 'content', 'parent']


@admin.register(PostLike)
class PostLikeAdmin(admin.ModelAdmin):
  list_display = ['id', 'user', 'post']


@admin.register(CommentLike)
class CommentLikeAdmin(admin.ModelAdmin):
  list_display = ['id', 'user', 'comment']


@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
  list_display = ['id', 'user', 'post']