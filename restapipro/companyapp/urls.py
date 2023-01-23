from django.urls import path,include
from django.views.generic import TemplateView

from .import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('secretuser', views.secretall, basename='user_api')
app_name = 'companyapp'

urlpatterns = [

    path('secretall/', views.secretall.as_view(), name='secretall'),
    path('createprivate/', views.createprivate.as_view(), name='private'),
    path('secretall/update/<int:pk>/', views.update.as_view(), name='update'),
    path('create/', views.create, name='create'),

]