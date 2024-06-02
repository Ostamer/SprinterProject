from django.shortcuts import render
from rest_framework import generics

from SpriterReact.models import SpUser
from SpriterReact.serializers import AuthSerializer


# Create your views here.
class AuthAPIView(generics.ListAPIView):
    queryset = SpUser.objects.all()
    serializer_class = AuthSerializer