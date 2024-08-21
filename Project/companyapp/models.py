from django.contrib.auth.hashers import make_password
from django.db import models
'''from django_encrypt_decrypt import EncryptedBinaryField

password = EncryptedBinaryField(max_length=100)
'''

class PrivateBox(models.Model):
    name = models.CharField(max_length=45)
    company_name = models.CharField(max_length=200)
    company_code = models.IntegerField(unique=True)
    company_email = models.EmailField(max_length=100,unique=True)
    password =  models.CharField(max_length=100)
    api_key = models.CharField(max_length=500)
    #expiration_date=models.DateTimeField()

    def save(self, *args, **kwargs):
        self.s_password = make_password(self.password)
        super(PrivateBox, self).save(*args, **kwargs)

    class Meta:
        managed = False
        db_table = 'private_tb'