from django.urls import path
from .views import create_post, edit_post, view_posts, view_my_posts, create_comment, view_comments, reply_to_comments, like_post, like_comment, bookmark

urlpatterns = [
  path('posts/create/', create_post, name="create_post"),
  path('posts/<int:post_id>/edit/', edit_post, name='edit_post'),
  path('posts/', view_posts, name="view_posts"),
  path('posts/my_posts/', view_my_posts, name="view_my_posts"),
  path('posts/<int:post_id>/comment/', create_comment, name="create_comment"),
  path('posts/<int:post_id>/comments/', view_comments, name="view_comments"),
  path('comments/<int:comment_id>/reply/', reply_to_comments, name="reply_to_comments"),
  path('posts/<int:post_id>/like/', like_post, name="like_post"),
  path('comments/<int:comment_id>/like/', like_comment, name="like_comment"),
  path('posts/<int:post_id>/bookmark/', bookmark, name="bookmark_post")
]