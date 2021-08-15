from django.contrib import admin
from django.urls.conf import include
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login', views.login1, name="login"),
    path('profile', views.profile, name="profile"),
    path('register/', views.register, name='register'),
    path('otp/', views.otp, name="otp"),
    path('fav/<int:id>/', views.favourite_add, name="favourite_add"),
    path('favourites', views.favourite_list, name="favourite_list"),
    path('update', views.update, name='update'),
    path('test', views.test, name="test"),
    path('personal_info_add', views.personal_info_add, name="personal_info_add")
    #     path('profile/', views.profile, name='profile'),
    #     path('logn', auth_views.LoginView.as_view(template_name='login.html'), name='login2'),
    #     path('logout/', auth_views.LogoutView.as_view(template_name='register/logout.html'), name='logout'),
    #     path('password-reset/',
    #          auth_views.PasswordResetView.as_view(
    #              template_name='register/password_reset.html'
    #          ),
    #          name='password_reset'),
    #     path('password-reset/done/',
    #          auth_views.PasswordResetDoneView.as_view(
    #              template_name='register/password_reset_done.html'
    #          ),
    #          name='password_reset_done'),
    #     path('password-reset-confirm/<uidb64>/<token>/',
    #          auth_views.PasswordResetConfirmView.as_view(
    #              template_name='register/password_reset_confirm.html'
    #          ),
    #          name='password_reset_confirm'),
    #     path('password-reset-complete/',
    #          auth_views.PasswordResetCompleteView.as_view(
    #              template_name='register/password_reset_complete.html'
    #          ),
    #          name='password_reset_complete'),
    #          path("send_otp",views.send_otp,name="send otp"),
]
