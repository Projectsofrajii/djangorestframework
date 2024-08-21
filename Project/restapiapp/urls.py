from django.urls import path,include
from django.views.generic import TemplateView

from .import views


app_name = 'restapiapp'

urlpatterns = [
    path('getall/', views.getall.as_view(), name='getall'),
    path('getall/create/', views.create.as_view(), name='create'),
    path('getall/getid/<int:pk>/', views.getbyid.as_view(), name='get'),
    path('getall/update/<int:pk>/', views.update.as_view(), name='update'),
    path('getall/delete/<int:pk>/', views.delete.as_view(), name='delete'),
    path('getall/destroy/<int:pk>/', views.destroy, name='destroy'),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path('devnote_api/', views.devnote_api, name='devnote_api'),


]
# path("destroy/<int:pk>/", TemplateView.as_view(template_name="api_serializer/delete.html"), name="testboot"),

