from django.contrib.auth.models import User
from .models import information
from django.forms import forms

class infoform(forms.Form):

    class Meta:
        model = information
        fields = ['user_id', 'name','email', 'contact' ,'aadharno' , 'address']