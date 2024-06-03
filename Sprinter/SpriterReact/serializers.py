from rest_framework import serializers

from SpriterReact.models import SpUser


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
