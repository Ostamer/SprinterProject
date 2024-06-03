from django.contrib.auth import authenticate
from rest_framework import serializers

from SpriterReact.models import SpUser, Post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpUser
        fields = ['login', 'password', 'first_name', 'last_name', 'middle_name', 'last_login']
        extra_kwargs = {
            'password': {'write_only': True}  # Указываем, что поле пароля не должно быть доступно для чтения
        }

    def create(self, validated_data):
        return SpUser.objects.create_user(**validated_data)


class CheckLoginSerializer(serializers.Serializer):
    login = serializers.EmailField()

    def validate_login(self, value):
        return value


class LoginSerializer(serializers.Serializer):
    login = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        login = data.get('login')
        password = data.get('password')
        user = authenticate(login=login, password=password)
        if user and user.is_active:
            data['user'] = user
            return data
        raise serializers.ValidationError("Unable to log in with provided credentials.")

class UserFIOSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpUser
        fields = ["last_name", "middle_name", "first_name"]
class PostSerializer(serializers.ModelSerializer):
    user = UserFIOSerializer()
    class Meta:
        model = Post
        fields = ["post_id", "title", "small_text", "likes_count", "user"]