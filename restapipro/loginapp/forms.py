from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from rest_framework import  serializers
from django.forms import ModelForm

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

