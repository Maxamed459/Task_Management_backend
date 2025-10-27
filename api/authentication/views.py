from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import APIView, api_view
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from rest_framework import status
from .serializers import UserLoginSerializer, UserSerializer
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token


class Index(APIView):
    permission_classes = [AllowAny]
    def get(self, request, *args, **kwargs):
        return Response({
            "message": "Hi welcome the authentication api v1 here you can make register, login you can register using username, email and password and you can login using username and password"
        }, status=status.HTTP_200_OK)


class UserRegistration(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user_data = UserSerializer(user).data
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                "user": user_data,
                "token": token.key,
                "message": "User created successfully!"
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLogin(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            token, _ = Token.objects.get_or_create(user=user)
            user_data = UserLoginSerializer(user).data
            return Response({
                "user": user_data,
                "token": token.key,
                "message": "Logged in successfully"
            })
        
        return Response({
            "message": "Invalid username or password"
        }, status=status.HTTP_400_BAD_REQUEST)
        
