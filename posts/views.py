from django.shortcuts import render
from .serializers import CreatePostSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
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