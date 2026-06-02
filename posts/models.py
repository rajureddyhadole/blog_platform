from django.db import models
from django.conf import settings
# Create your models here.
class Post(models.Model):

  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

  title = models.TextField()
  content = models.TextField()

  class Status(models.TextChoices):
    PUBLISHED = "published", "Published"
    DRAFT = "draft", "Draft"
  
  status = models.CharField(
    max_length=20,
    choices=Status.choices,
    default=Status.DRAFT
  )
  
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title



class Comment(models.Model):

  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  content = models.TextField()

  parent = models.ForeignKey(
    'self',
    on_delete=models.CASCADE,
    blank=True,
    null=True,
    related_name="children"
  )

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f"reply to comment #{self.id}"



class PostLike(models.Model):

  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  post = models.ForeignKey(Post, on_delete=models.CASCADE)



class CommentLike(models.Model):

  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  comment = models.ForeignKey(Comment, on_delete=models.CASCADE)



class Bookmark(models.Model):

  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  post = models.ForeignKey(Post, on_delete=models.CASCADE)