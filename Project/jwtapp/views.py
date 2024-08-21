import datetime
import jwt
from rest_framework.authentication import get_authorization_header
from rest_framework.exceptions import AuthenticationFailed, APIException
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import Userserializer
from .models import User
from .authentication import create_access_token,create_refresh_token,decode_access_token,decode_refresh_token

class Register(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'signup.html'
    def post(self,request):
        serializer = Userserializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class Logins(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'signin.html'
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('user not found')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect Password')

        payload = {
            'email' : user.email,
            'username': user.username,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
        }
        token = jwt.encode(payload,'SECRET_KEY',algorithm='HS256')
        decode= jwt.decode(token, 'SECRET_KEY', algorithms=["HS256"])
        #decode = jwt.decode(token)
        return Response({'jwt' : token,'decode' : decode})

class Login(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'signin.html'
    def post(self, request):
        user = User.objects.filter(email=request.data['email']).first()

        if not user:
            raise APIException('Invalid Credentials')

        if not user.check_password(request.data['password']):
            raise APIException('Invalid Credentials')

        access_token = create_access_token(user.id)
        refresh_token = create_refresh_token(user.id)

        response = Response()
        response.set_cookie(key='refreshToken',value=refresh_token,httponly=True)
        response.data ={
            'token' : access_token,'access_token' : refresh_token
        }
        return response

class UserAPIView(APIView):
    def get(self, request):
        auth = get_authorization_header(request).split()

        if auth and len(auth) == 2:
            token = auth[1].decode('utf-8')
            id = decode_access_token(token)
            user = User.objects.filter(pk=id).first()
            return Response(Userserializer(user).data)
        raise AuthenticationFailed('unauthorized')

class RefreshAPIView(APIView):
    def post(self, request):
        refresh_token = request.COOKIES.get('refreshtoken')
        id = decode_refresh_token(refresh_token)
        access_token = create_access_token(id)
        return Response ({
            'token' : access_token
        })

class logoutAPIView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie(key="refreshToken")
        response.data = {
            'message'  : 'success'
        }
        return Response