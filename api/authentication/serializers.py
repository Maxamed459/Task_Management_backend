from .models import User
from rest_framework import serializers
from django.contrib.auth import authenticate, login
from rest_framework.validators import UniqueValidator
from rest_framework.exceptions import AuthenticationFailed

class UserRegistrationSerializer (serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, max_length=68, min_length=8)
    confirmation = serializers.CharField(write_only=True, max_length=68, min_length=8)
    access_token = serializers.CharField(max_length=255, read_only=True)
    refresh_token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ['id','first_name', 'last_name', 'email', 'password', 'confirmation', 'access_token', 'refresh_token']

    def validate(self, validated_data):
        if validated_data["password"] != validated_data["confirmation"]:
            raise serializers.ValidationError("passwords must match")
        if User.objects.filter(email=validated_data["email"]).exists():
            raise serializers.ValidationError("email already exists")
        return validated_data


    def create(self, validated_data):
        validated_data.pop("confirmation")
        user = User.objects.create_user(
            first_name = validated_data["first_name"],
            last_name = validated_data["last_name"],
            email = validated_data["email"],
            password = validated_data["password"],
        )
        user_tokens = user.tokens()
        return {
            "user": {
                "id": user.id,
                "email": user.email,
                "full_name": user.get_full_name
            },
            "access_token": str(user_tokens.get("access")),
            "refresh_token": str(user_tokens.get("refresh"))
        }
        

class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=6)
    password = serializers.CharField(max_length=68, min_length=8, write_only=True)
    full_name = serializers.CharField(max_length=255, read_only=True)
    access_token = serializers.CharField(max_length=255, read_only=True)
    refresh_token = serializers.CharField(max_length=255, read_only=True)
    class Meta:
        model = User
        fields = ['id', 'full_name', 'email', 'password', 'access_token', 'refresh_token']

    def validate(self, validated_data):
        email = validated_data.get("email")
        password = validated_data.get("password")
        request = self.context.get("request")
        user = authenticate(request, email=email, password=password)
        if not user:
            raise AuthenticationFailed("Invalid credentials try again")
        if not user.is_verified:
            raise AuthenticationFailed("email is not verified")
        
        user_tokens = user.tokens()

        return {
            "data": {
                "user": {
                "id": user.id,
                "email": user.email,
                "full_name": user.get_full_name
            },
            "access_token": str(user_tokens.get("access")),
            "refresh_token": str(user_tokens.get("refresh"))
            } 
        }


    