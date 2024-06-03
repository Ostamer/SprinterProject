from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import views, status
from rest_framework_simplejwt.tokens import RefreshToken

from SpriterReact.models import SpUser, Post
from SpriterReact.serializers import UserSerializer, CheckLoginSerializer, LoginSerializer, PostSerializer, \
    PostCreateSerializer


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

class LoginView(views.APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response(serializer.errors, status=400)

class PostListView(generics.ListAPIView): # для отображения ленты
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostCreateView(generics.CreateAPIView): # для создания поста
    serializer_class = PostCreateSerializer

class PostGetView(generics.ListAPIView):
    def get(self, request, post_id):
        post = Post.objects.filter(post_id=post_id).first()
        if not post:
            return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = PostSerializer(post)
        return Response(serializer.data)