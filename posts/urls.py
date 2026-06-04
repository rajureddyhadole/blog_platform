from django.urls import path
from .views import create_post, edit_post, view_posts, view_my_posts, create_comment, view_comments, reply_to_comments, like_post, like_comment

urlpatterns = [
  path('posts/create/', create_post, name="create_post"),
  path('posts/edit/<int:pk>/', edit_post, name='edit_post'),
  path('posts/', view_posts, name="view_posts"),
  path('posts/my_posts/', view_my_posts, name="view_my_posts"),
  path('posts/<int:pk>/comment/', create_comment, name="create_comment"),
  path('posts/<int:pk>/comments/', view_comments, name="view_comments"),
  path('comments/<int:pk>/reply/', reply_to_comments, name="reply_to_comments"),
  path('posts/<int:post_id>/like/', like_post, name="like_post"),
  path('comments/<int:comment_id>/like/', like_comment, name="like_comment"),
]