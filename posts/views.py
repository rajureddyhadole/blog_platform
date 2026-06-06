from django.shortcuts import render
from .serializers import CreatePostSerializer, EditPostSerializer, ViewPostsSerializer, ViewMyPostsSerializer, CreateCommentSerializer, ViewCommentsSerializer, ReplyToCommentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from .models import Post, Comment, PostLike, CommentLike, Bookmark
from django.db.models import Q
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
def edit_post(request, post_id):

  post = get_object_or_404(Post, id=post_id, author=request.user)
  
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

  author_param = request.query_params.get('author')
  search_param = request.query_params.get('search')

  if author_param:

    posts = posts.filter(author__username__iexact=author_param)
  
  if search_param:

    posts = posts.filter(
      Q(title__icontains=search_param) | Q(content__icontains=search_param)
    )

  serializer = ViewPostsSerializer(posts, many=True)

  return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_my_posts(request):
  
  posts = Post.objects.filter(author=request.user)

  serializer = ViewMyPostsSerializer(posts, many=True)

  return Response(serializer.data)




#####################Comment APIs##################
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_comment(request, post_id):

  post = get_object_or_404(Post, id=post_id)

  serializer = CreateCommentSerializer(
    data=request.data,
    context={
      'request': request,
      'post': post
    }
  )

  if serializer.is_valid():

    serializer.save()

    return Response({
      'message': 'commented on the post successfully',
      'data': serializer.data
      })
  
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_comments(request, post_id):
  
  comments = Comment.objects.filter(
    post_id=post_id
  )

  serializer = ViewCommentsSerializer(comments, many=True)

  return Response(serializer.data)




@api_view(['POST'])
@permission_classes([IsAuthenticated])
def reply_to_comments(request, comment_id):
  
  comment = get_object_or_404(Comment, id=comment_id)

  post = comment.post

  serializer = ReplyToCommentSerializer(data=request.data, context={'request': request, 'post': post, 'comment': comment})

  if serializer.is_valid():

    serializer.save()

    return Response({
      'message': 'reply is done successfully',
      'data': serializer.data
    })
  
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




##############post like api ######################

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_post(request, post_id):
  
  post = get_object_or_404(Post, id=post_id)

  user = request.user

  try:
    like_exists = PostLike.objects.get(user=user, post=post)
  except PostLike.DoesNotExist:
    like_exists = None

  if like_exists:

    like_exists.delete()
    
    return Response({
      'message': "you disliked the post",
      'user': like_exists.user.id,
      'post': like_exists.post.id
    })

  like = PostLike.objects.create(
    user=user,
    post=post
  )

  return Response({
    'message': 'liked a post successfully',
    'id': like.id,
    'user': like.user.id,
    'post': like.post.id
  }, status=status.HTTP_201_CREATED)



############# comment like api ########################
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_comment(request, comment_id):
  
  comment = get_object_or_404(Comment, id=comment_id)

  user = request.user

  like_exists = CommentLike.objects.filter(user=user, comment=comment).first()
  
  if like_exists:

    like_exists.delete()

    return Response({
      'message': "You have unliked the comment",
      'user': like_exists.user.id,
      'comment': like_exists.comment.id
    })
  
  like = CommentLike.objects.create(
    user=user,
    comment=comment
  )

  return Response({
    'message': "you have liked this comment",
    'user': like.user.id,
    'comment': like.comment.id
  }, status=status.HTTP_201_CREATED)




################ bookmark api ##################
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def bookmark(request, post_id):
  
  post = get_object_or_404(Post, id=post_id)

  bookmark_exists = Bookmark.objects.filter(user=request.user, post=post).first()

  if bookmark_exists:

    bookmark_exists.delete()

    return Response({
      'message': 'bookmark is removed successfully',
      'user': bookmark_exists.user.id,
      'post': bookmark_exists.post.id
    })
  
  bookmark = Bookmark.objects.create(
    user=request.user,
    post=post
  )

  return Response({
    'message': "bookmark added successfully",
    'user': bookmark.user.id,
    'post': bookmark.post.id
  })
