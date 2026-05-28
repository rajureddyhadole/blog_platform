from django.contrib import admin
from .models import Post
# Register your models here.
@admin.register(Post)
class Post(admin.ModelAdmin):
  list_display = ['id', 'title', 'content', 'status']
  list_filter = ['status']
  search_fields = ['title', 'content']