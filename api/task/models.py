from django.db import models
from authentication.models import User

class Task(models.Model):

    PRIORITY_CHOICES = [
        ("low", "LOW"),
        ("medium", "MEDIUM"),
        ("high", "HIGH")
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="task_owner")
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.priority.capitalize()})"
