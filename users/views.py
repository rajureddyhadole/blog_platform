from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import permissions
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer, LoginSerializer
from django.contrib.auth import authenticate
# Create your views here.

@api_view(['POST'])
def register(request):

  serializer = RegisterSerializer(data=request.data)

  if serializer.is_valid():

    serializer.save()

    return Response({
      'message': "User has been registered successfully",
      'data': serializer.data
    })
  
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login_view(request):
  
  serializer = LoginSerializer(data=request.data)

  if serializer.is_valid():

    user = authenticate(
      username=serializer.validated_data['username'],
      password=serializer.validated_data['password']
    )

    if user is not None:
      refresh = RefreshToken.for_user(user)

      return Response({
        'access': str(refresh.access_token),
        'refresh': str(refresh),
        'user': {
          'id': user.id,
          'username':user.username,
          'email': user.email
        }
      })
    
    return Response({'message': 'user not found!'}, status=status.HTTP_401_UNAUTHORIZED)
  
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)