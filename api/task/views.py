from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from .serializers import TaskSerializer
from .models import Task
import datetime


@api_view(["GET"])
def index(request, *args, **kwargs):
    return Response({
        "message": "Hi User, welcome to the task API v1"
    })


class TaskCreateAPIView(generics.CreateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def perform_create(self, serializer):
        title = serializer.validated_data.get("title")
        description = serializer.validated_data.get("description")
        due_date = serializer.validated_data.get("due_date")
        if description is None:
            description = title
        if due_date is None:
            due_date = datetime.date.today()
        serializer.save(owner=self.request.user, description=description, due_date=due_date)


class ListTaskAPIView(generics.ListAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def get_queryset(self):
        user = self.request.user
        if not user.is_authenticated:
            return Task.objects.none()
        return Task.objects.filter(owner=user)
