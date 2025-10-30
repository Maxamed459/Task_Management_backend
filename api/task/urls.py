from django.urls import path
from . import views

urlpatterns = [
    path("index/", views.index, name="task-index"),
    path("", views.TaskCreateListAPIView.as_view(), name="task-list-create"),
    path("<int:pk>/", views.TaskDetailAPIView.as_view(), name="task-detail"),
]