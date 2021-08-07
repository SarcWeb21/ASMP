from django.urls import path
from . import views

urlpatterns = [
    path('home', views.index, name="index"),
    path('fav/<int:id>/', views.favourite_add, name="favourite_add"),
    path('favourites', views.favourite_list, name="favourite_list"),
    path('update', views.update, name='update')
]
