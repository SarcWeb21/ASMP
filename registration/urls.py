from django.urls import path
from . import views

urlpatterns = [
    path('home', views.index, name = "index"),
    path('login', views.login, name = "login"),
    path('profile', views.profile, name="profile")
]