from django.contrib.auth.models import User
from .models import information
from rest_framework import  serializers


class infoserializer(serializers.ModelSerializer):

    class Meta:
        model = information
        fields = ['id','user_id', 'name','email', 'contact' ,'aadharno' , 'address']