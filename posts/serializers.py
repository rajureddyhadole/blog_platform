from rest_framework import serializers
from .models import Post, Comment

class CreatePostSerializer(serializers.ModelSerializer):

  class Meta:
    model = Post
    fields = ['id', 'title', 'content', 'status']

  def create(self, validated_data):

    post = Post.objects.create(
      author=self.context['request'].user,
      title=validated_data['title'],
      content=validated_data['content'],
      status=validated_data['status']
    )

    return post
  


class EditPostSerializer(serializers.ModelSerializer):

  class Meta:
    model = Post
    fields = ['id', 'title', 'content', 'status']



class ViewPostsSerializer(serializers.ModelSerializer):

  class Meta:
    model = Post
    fields = ['id', 'title', 'content', 'status']
  

class ViewMyPostsSerializer(serializers.ModelSerializer):

  class Meta:
    model = Post
    fields = ['id', 'title', 'content', 'status']



############# Comment Serializers #################

class CreateCommentSerializer(serializers.ModelSerializer):

  class Meta:
    model = Comment
    fields = ['id','author', 'post', 'content']

    extra_kwargs = {
      'author': {'read_only': True},
      'post': {'read_only': True}
    }

  def create(self, validated_data):

    comment = Comment.objects.create(
      author=self.context['request'].user,
      post=self.context['post'],
      content=validated_data['content']
    )

    return comment
  


class ViewCommentsSerializer(serializers.ModelSerializer):

  class Meta:
    model = Comment
    fields = ['id', 'author', 'post', 'content']


class ReplyToCommentSerializer(serializers.ModelSerializer):

  class Meta:
    model = Comment
    fields = ['id', 'author', 'post', 'content', 'parent']

    extra_kwargs = {
      'author': {'read_only': True},
      'post': {'read_only': True},
      'parent': {'read_only': True}
    }

  def create(self, validated_data):

    comment = Comment.objects.create(
      author=self.context['request'].user,
      post=self.context['post'],
      content=validated_data['content'],
      parent=self.context['comment']
    )

    return comment
