from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import permissions
from rest_framework import status
from .serializers import RegisterSerializer
# Create your views here.

@api_view(['POST'])
def register(request):

  serializer = RegisterSerializer(data=request.data)

  if serializer.is_valid():

    return Response({
      'message': "User has been registered successfully",
      'data': serializer.data
    })
  
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)