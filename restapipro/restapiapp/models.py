from django.db import models

class information(models.Model):
    #user = models.OneToOneField("authapp.CustomUser", on_delete=models.CASCADE)
    user_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    contact = models.BigIntegerField()
    aadharno = models.CharField(max_length=50)
    address = models.CharField(max_length=30)

