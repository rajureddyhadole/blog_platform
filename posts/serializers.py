from rest_framework import serializers
from .models import Post

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