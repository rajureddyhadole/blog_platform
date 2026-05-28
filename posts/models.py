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