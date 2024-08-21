from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView
from rest_framework_simplejwt import authentication
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import information
from .serializers import infoserializer
'''
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser,AllowAny]
    authentication_classes = (authentication.JWTAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)'''

@csrf_exempt
@api_view(["GET"])
def devnote_api(request):
    data = "How to Implement Token-based authentication using Django"
    return Response({'data': data}, status=HTTP_200_OK)

class getall(APIView): #all done
    authentication_classes = [SessionAuthentication, BasicAuthentication,TokenAuthentication]
    permission_classes = [IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'api_serializer/getall.html'

    def get(self, request):
        try:
            queryset = information.objects.all()
            return Response({'dataset': queryset})
        except:
            return HttpResponse('You are not authorized', status=401)

class create(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication,TokenAuthentication]
    permission_classes = [IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'api_serializer/create.html'

    def get(self,request):
        serializer = infoserializer()
        return Response({'serializer': serializer})

    def post(self, request):
        try:
            serializer = infoserializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'serializer': serializer})
            return redirect('http://127.0.0.1:8000/getall/')
        except:
            return HttpResponse('You are not authorized', status=401)

class update(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication,TokenAuthentication]
    permission_classes = [IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'api_serializer/update.html'

    def get(self, request, pk):
        query = get_object_or_404(information, pk=pk)
        serializer = infoserializer(query)
        return Response({'serializer': serializer, 'query':query})

    def post(self, request, pk):
        query = get_object_or_404(information, pk=pk)
        serializer = infoserializer(query, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'query': query})
        serializer.save()
        return redirect('http://127.0.0.1:8000/getall/')

class getbyid(APIView): #done
    authentication_classes = [SessionAuthentication, BasicAuthentication,TokenAuthentication]
    permission_classes = [IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'api_serializer/getid.html'

    def get(self, request, pk):
        query = get_object_or_404(information, pk=pk)
        serializer = infoserializer(query)
        return Response({'serializer': serializer, 'query': query})

def destroy(request, pk):

    user = information.objects.get(pk=pk)
    user.delete()
    return redirect(request,'http://127.0.0.1:8000/getall/')

class deletes(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication,TokenAuthentication]
    permission_classes = [IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'api_serializer/delete.html'

    def get(self, request,pk):
        queryset = information.objects.get(pk=pk)
        return Response({'data': queryset})

class delete(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication,TokenAuthentication]
    permission_classes = [IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'api_serializer/delete.html'

    def get(self, request, pk):
        try:
            query = get_object_or_404(information, pk=pk)
            serializer = infoserializer(query)
            return Response({'serializer': serializer, 'query': query})
        except:
            return Response({'You are not authorized'})

'''    messages.success(request, 'Delete Successfully')'''
