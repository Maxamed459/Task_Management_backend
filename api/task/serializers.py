from rest_framework import serializers
from .models import Task
from rest_framework.validators import UniqueValidator

class TaskSerializer(serializers.ModelSerializer):

    owner = serializers.CharField(read_only=True)

    class Meta:
        model = Task
        fields = ["owner", "id", "title", "description", "due_date", "priority", "is_completed", "created_at", "updated_at"]

    def get_owner(self, obj):
        request = self.context.get("request")
        return request.user.username
        


