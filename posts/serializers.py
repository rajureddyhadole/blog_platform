from rest_framework import serializers
from .models import Post, Comment

class PostsSerializer(serializers.ModelSerializer):

  class Meta:
    model = Post
    fields = ['id', 'title', 'content', 'status']


############# Comment Serializers #################

class CommentSerializer(serializers.ModelSerializer):

  class Meta:
    model = Comment
    fields = ['id','author', 'post', 'content']

    extra_kwargs = {
      'author': {'read_only': True},
      'post': {'read_only': True}
    }  


class ReplyToCommentSerializer(serializers.ModelSerializer):

  class Meta:
    model = Comment
    fields = ['id', 'author', 'post', 'content', 'parent']

    extra_kwargs = {
      'author': {'read_only': True},
      'post': {'read_only': True},
      'parent': {'read_only': True}
    }