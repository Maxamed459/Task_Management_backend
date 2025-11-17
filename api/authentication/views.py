from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from .serializers import UserLoginSerializer, UserRegistrationSerializer
from rest_framework.permissions import AllowAny


class Index(GenericAPIView):
    permission_classes = [AllowAny]
    def get(self, request, *args, **kwargs):
        return Response({
            "message": "Hi welcome the authentication api v1 here you can make register, login you can register using username, email and password and you can login using username and password"
        }, status=status.HTTP_200_OK)


class UserRegistration(GenericAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]
    def post(self, request):
        user_data = request.data
        serializer = self.get_serializer(data = user_data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response({
                "data": user,
                "message": f"Hi Thunk you for registering, welcome to the Tasky platform."
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLogin(GenericAPIView):
    serializer_class = UserLoginSerializer
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
    
        
