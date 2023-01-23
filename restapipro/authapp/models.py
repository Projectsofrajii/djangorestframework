from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken

#creates auth_token table
'''def tokens(self):
    refresh = RefreshToken.for_user(self)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token)
    }'''