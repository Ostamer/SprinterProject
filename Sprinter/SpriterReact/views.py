from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import views, status
from rest_framework_simplejwt.tokens import RefreshToken

from SpriterReact.models import SpUser
from SpriterReact.serializers import UserSerializer, CheckLoginSerializer


# Create your views here.
class SignUpView(views.APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({"refresh" : str(refresh), "access" : str(refresh.access_token),}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class CheckLoginRegisteredView(views.APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = CheckLoginSerializer(data=request.data)
        if serializer.is_valid():
            login = serializer.validated_data['login']
            is_registered = SpUser.objects.filter(login=login).exists()
            return Response({"exists": is_registered}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)