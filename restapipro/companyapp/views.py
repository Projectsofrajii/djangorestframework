from datetime import timedelta

from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.utils.timezone import now
from django.views.generic import CreateView
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rich.markup import render

from .serializers import companyserializer
from .models import PrivateBox
from .encrypt import *

def create(request):
    if request.method == 'POST':
        serializer = companyserializer()
        name = request.POST['name']
        company_name = request.POST['company_name']
        company_code = request.POST['company_code']
        company_email = request.POST['company_email']
        password = encrypt(request.POST['password'])

        data = PrivateBox(name=name, company_name=company_name, company_code=company_code,
                          company_email=company_email,
                          password=password)
        data.save()
        return HttpResponse('Done')
    else:
        return render(request, 'secret/private.html')


class createsecretall(APIView): #all done
    authentication_classes = [SessionAuthentication, BasicAuthentication,TokenAuthentication]
    permission_classes = [IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'secret/getallprivate.html'

    def create(request):
        serializer = companyserializer()
        if request.method == "POST":
            key = Fernet.generate_key()
            name = request.POST['name']
            company_name = request.POST['company_name']
            company_code = request.POST['company_code']
            company_email = request.POST['company_email']
            password = key.encrypt(request.POST['password'])

            if serializer.is_valid():
                user = serializer.save(commit=False)
                user.password = make_password(user.password)
                user.save()


class secretall(APIView): #all done
    authentication_classes = [SessionAuthentication, BasicAuthentication,TokenAuthentication]
    permission_classes = [IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'secret/getallprivate.html'

    def get(self, request):
        secret = PrivateBox.objects.all()
        return Response({'secret': secret})

class createprivate(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication,TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'secret/private.html'

    def get(self,request):
        serializer = companyserializer()
        return Response({'serializer': serializer})

    def post(self, request):
        name = request.POST['name']
        company_name = request.POST['company_name']
        company_code = request.POST['company_code']
        company_email = request.POST['company_email']
        password = encrypt(request.POST['password'])
        serializer = companyserializer(data=request.data,name=name,company_name=company_name,
                                       company_code=company_code,company_email=company_email,
                                       password=password)
        if serializer.is_valid():
            serializer.save()
            return Response({'serializer': serializer})
        return redirect('companyapp:secretall')

class update(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication,TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'secret/sec_update.html'

    def get(self, request, pk):
        query = get_object_or_404(PrivateBox, pk=pk)
        serializer = companyserializer(query)
        return Response({'serializer': serializer, 'query':query})

    def post(self, request, pk):
        query = get_object_or_404(PrivateBox, pk=pk)
        serializer = companyserializer(query, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'query': query})
        serializer.save()
        return redirect('http://127.0.0.1:8000//companyapp/secretall/')
    '''if you are a superuser you can edit else not..'''

class delete(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication,TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'secret/delete.html'
    def delete(self,request, pk):
        user = PrivateBox.objects.get(pk=pk)
        user.delete()
        messages.success(request, 'deleted Successfully..')
