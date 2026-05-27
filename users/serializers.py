from .models import CustomUser
from rest_framework import serializers


class RegisterSerializer(serializers.ModelSerializer):

  class Meta:
    model = CustomUser
    fields = ['username', 'password', 'email', 'bio', 'date_of_birth']

    extra_kwargs = {
      'password': {
        'write_only': True
      }
    }
  
  def create(self, validated_data):

    user = CustomUser.objects.create_user(
      username=validated_data['username'],
      password=validated_data['password'],
      email=validated_data['email'],
      bio=validated_data['bio'],
      date_of_birth=validated_data['date_of_birth']
    )

    return user
  

class LoginSerializer(serializers.Serializer):

  username = serializers.CharField()

  password = serializers.CharField(
    write_only = True
  )