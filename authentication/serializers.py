from rest_framework import serializers
from django.contrib.auth import get_user_model

# Serializer for User Registration
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ['username', 'password', 'email', 'first_name', 'last_name']

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user

# Serializer for User Login
class UserLogInSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
