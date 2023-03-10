from django.shortcuts import render
from rest_framework import generics,status,views
from rest_framework.renderers import TemplateHTMLRenderer

from .serializers import RegisterSerializer,EmailVerificationSerializer,LoginSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from .utils import Util
from django.contrib.sites.shortcuts import get_current_site
from rest_framework.authtoken import views
from django.urls import reverse
import jwt
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse
from .encrypt import *
from .models import Login,User,EmpLogin

class RegisterView(generics.GenericAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'token/signup.html'
    serializer_class = RegisterSerializer
    def post(self,request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        user = User.objects.get(email = user_data['email'])
        token = RefreshToken.for_user(user).access_token
        current_site = get_current_site(request).domain
        relativeLink =reverse('email-verify')
        absurl = 'http://'+current_site+relativeLink+"?token="+str(token)
        email_body = 'Hi' +user.username+'Use link below to verify your email \n' + absurl
        data = {'email_body': email_body,'to_email': user.email,
                'email_subject':'Verify your email'}
        #Util.send_email(data)
        return Response(user_data,status.HTTP_201_CREATED,data)

class VerifyEmail(views.APIView):

    serializer_class = EmailVerificationSerializer

    def get(self,request):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(token,settings.SECRET_KEY)
            user = User.objects.get(id=payload['user_id'])
            if not user.is_verified:
                user.is_verified = True
                user.save()
            return Response({'email' :'Successfully activated'},status = status.HTTP_200_OK)
        except jwt.ExpiredSignatureError:
            return Response({'error': 'Activation Expired'},status = status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError:
            return Response({'error':'Invalid token'},status = status.HTTP_400_BAD_REQUEST)

class loginAPIView(generics.GenericAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = '/signin.html'
    serializer_class = LoginSerializer

    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        encryptedpassword=make_password(request.POST['password'])
        print(encryptedpassword)
        checkpassword=check_password(request.POST['password'], encryptedpassword)
        print(checkpassword)
        data=Login(email=email, password=encryptedpassword)

        data.save()
        return HttpResponse('Done')
    else:
        return render(request, 'encrypt.html')


def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = encrypt(request.POST['password'])
        print('Original Password:', request.POST['password'])
        encryptpass= encrypt(request.POST['password'])
        print('Encrypt Password:',encryptpass)
        decryptpass= decrypt(encryptpass)
        print('Decrypt Password:',decryptpass)
        data=EmpLogin(name=name, email=email, password=password)
        data.save()
        return HttpResponse('Done')
    else:
        return render(request, 'reg_encrypt.html')


