from rest_framework import serializers

from SpriterReact.models import SpUser


class AuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpUser
        fields = '__all__'
