from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken

class User(AbstractBaseUser):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    #is_active = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.email

   # create authtoken_token table
    def tokens(self):
        tokens = RefreshToken.for_user(self)
        return {
            'refresh':str(tokens),
            'access': str(tokens.access_token)
        }
    class Meta:
        managed = False
        db_table = 'user'



class Login(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table="Login"

class EmpLogin(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table="EmpLogin"