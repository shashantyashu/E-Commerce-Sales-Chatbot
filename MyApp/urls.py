from django.contrib import admin
from django.urls import path
from MyApp import views

urlpatterns = [
    path('', views.index),
    path('explore/', views.index, name='index'),
    path('show/<str:id>/', views.show, name='show'),
    path('login', views.loginUser, name="login"),
    path('logout', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),
]