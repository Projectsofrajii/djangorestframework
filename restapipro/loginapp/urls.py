from django.urls import path
from django.views.generic import TemplateView

from .import views


urlpatterns = [
    path('signin/', views.signin,name='login'),
    path('signup/', views.signup, name='signup'),
    path('signout/', views.signout, name='logout'),
]