from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('register', views.UserRegistration.as_view(), name="register"),
    path('login', views.UserLogin.as_view(), name="login"),
    path('logout', views.logout, name="logout"),
]