from django.urls import path
from .views import create_post, edit_post, view_posts, view_my_posts

urlpatterns = [
  path('posts/create/', create_post, name="create_post"),
  path('posts/edit/<int:pk>/', edit_post, name='edit_post'),
  path('posts/', view_posts, name="view_posts"),
  path('posts/my_posts/', view_my_posts, name="view_my_posts"),
]