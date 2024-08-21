from django.urls import path
from django.views.generic import TemplateView
from rest_framework_simplejwt.views import TokenVerifyView, TokenObtainPairView, TokenRefreshView

from .import views

app_name = 'authapp'

urlpatterns = [

    path('login/', views.loginPage,name='login'),
    path('signup/', views.registerPage, name='signup'),
    path("resetpass/", views.resetpass, name="resetpass"),
    path('signout/', views.logoutUser, name='signout'),
    path("logout/", TemplateView.as_view(template_name="logout.html"), name="logout"),

    path('api/', TokenVerifyView.as_view(), name='token'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    #path('signin/', views.Login.as_view(), name='login'),

]