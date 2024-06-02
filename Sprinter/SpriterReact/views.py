from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from SpriterReact.models import SpUser
from SpriterReact.serializers import AuthSerializer


# Create your views here.
class AuthAPIView(APIView):

    def get(self, request):
        users = SpUser.objects.all().values()
        return Response({'users' : list(users)})

    def post(self, request):
        post_new = SpUser.objects.create(
            last_name = request.data['last_name'],
            first_name = request.data['first_name'],
            login = request.data['login'],
            user_password = request.data['user_password']
        )
        return Response({'post': model_to_dict(post_new)})