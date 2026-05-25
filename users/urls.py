from django.urls import path
from .views import register
from rest_framework_simplejwt.views import (
  TokenObtainPairView,
  TokenRefreshView
)

urlpatterns = [
  path('api/token/', TokenObtainPairView.as_view(), name='obtain_token'),
  path('api/token/refresh/', TokenRefreshView.as_view(), name="refresh_token"),
  path('register/', register, name="register")
]