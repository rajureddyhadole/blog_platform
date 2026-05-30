from django.shortcuts import render
from .serializers import CreatePostSerializer, EditPostSerializer, ViewPostsSerializer, ViewMyPostsSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from .models import Post
# Create your views here.

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_post(request):

  serializer = CreatePostSerializer(data=request.data, context={'request': request})

  if serializer.is_valid():

    serializer.save()

    return Response({
      'message':'Post created successfully.',
      'data': serializer.data
    })
  
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def edit_post(request, pk):

  post = get_object_or_404(Post, id=pk, author=request.user)
  
  serializer = EditPostSerializer(post, data=request.data, partial=True)

  if serializer.is_valid():

    serializer.save()

    return Response({
      'message': 'Post updated successfully',
      'data': serializer.data
    })
  
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_posts(request):

  posts = Post.objects.filter(status='published')

  serializer = ViewPostsSerializer(posts, many=True)

  return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_my_posts(request):
  
  posts = Post.objects.filter(author=request.user)

  serializer = ViewMyPostsSerializer(posts, many=True)

  return Response(serializer.data)