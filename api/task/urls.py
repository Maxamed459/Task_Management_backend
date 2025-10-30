from django.urls import path
from . import views

urlpatterns = [
    path("index", views.index, name="task-index"),
    path("create", views.TaskCreateAPIView.as_view(), name="create"),
    path("list", views.ListTaskAPIView.as_view(), name="list"),
]