from django.contrib import admin
from django.urls import path,include
from .import views
from django.urls import path
from .import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
app_name = 'jwtapp'

urlpatterns = [
    path('signup/', views.Register.as_view(), name='signup'),#register data
    path('login/', views.Login.as_view(), name='login'),  # register data
    path('logout/', views.logoutAPIView.as_view(), name='logout'),

    path('user/', views.UserAPIView.as_view(), name='token_obtain_pair'),
    path('refresh/', views.RefreshAPIView.as_view(), name='token_obtain_pair'),

    path('api/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


]

