from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from .serializers import TaskSerializer
from .models import Task
import datetime
from .permissions import IsOwnerOnly


@api_view(["GET"])
def index(request, *args, **kwargs):
    return Response({
        "message": "Hi User, welcome to the task API v1"
    })


class TaskCreateListAPIView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def get_queryset(self):
        return Task.objects.filter(owner = self.request.user)

    def perform_create(self, serializer):
        title = serializer.validated_data.get("title")
        description = serializer.validated_data.get("description")
        due_date = serializer.validated_data.get("due_date")
        if description is None:
            description = title
        if due_date is None:
            due_date = datetime.date.today()
        serializer.save(owner=self.request.user, description=description, due_date=due_date)\




class TaskDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsOwnerOnly]

    def get_queryset(self):
        return Task.objects.filter(owner = self.request.user)





