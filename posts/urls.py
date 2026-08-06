from django.urls import path
from .views import  edit_post, view_my_posts, reply_to_comments, like_post, like_comment, bookmark, post_list_create, comment_list_create

urlpatterns = [
  path('posts/', post_list_create),
  path('posts/<int:post_id>/', edit_post),
  path('posts/my_posts/', view_my_posts, name="view_my_posts"),
  path('posts/<int:post_id>/comments/', comment_list_create),
  path('comments/<int:comment_id>/reply/', reply_to_comments, name="reply_to_comments"),
  path('posts/<int:post_id>/like/', like_post, name="like_post"),
  path('comments/<int:comment_id>/like/', like_comment, name="like_comment"),
  path('posts/<int:post_id>/bookmark/', bookmark, name="bookmark_post")
]