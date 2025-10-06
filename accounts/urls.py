from django.urls import path
from .views import register, home, CustomLogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", home, name="home"),
    path("register/", register, name="register"),
    path("logout/",  CustomLogoutView.as_view(), name="logout"),
    path("login/", auth_views.LoginView.as_view(template_name="registeration/login.html"), name='login'),
]