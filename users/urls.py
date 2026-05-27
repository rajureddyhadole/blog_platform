from django.urls import path
from .views import register, login_view
from rest_framework_simplejwt.views import (
  TokenObtainPairView,
  TokenRefreshView
)

urlpatterns = [
  path('api/token/', TokenObtainPairView.as_view(), name='obtain_token'),
  path('api/token/refresh/', TokenRefreshView.as_view(), name="refresh_token"),
  path('register/', register, name="register"),
  path('login/', login_view, name='login')
]