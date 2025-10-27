from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import authenticate, login
from rest_framework.validators import UniqueValidator

class UserSerializer (serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirmation = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id','username', 'email', 'password', 'confirmation', 'date_joined']

    def validate(self, data):
        if data["password"] != data["confirmation"]:
            raise serializers.ValidationError("passwords must match")
        if User.objects.filter(email=data["email"]).exists():
            raise serializers.ValidationError("email already exists")
        return data
         

    def create(self, validated_data):
        validated_data.pop("confirmation")
        user = User.objects.create_user(
            username = validated_data["username"],
            email = validated_data["email"],
            password = validated_data["password"],
        )
        return user

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'date_joined']

    