from .models import PrivateBox
from rest_framework import  serializers

class companyserializer(serializers.ModelSerializer):

    class Meta:
        model = PrivateBox
        fields = ['name','company_name','company_code', 'company_email','password' ]