from django.contrib import admin
from django.urls import path,include
from app1 import views

urlpatterns = [
    path('',views.home_fun),
    path('Register/',views.login_fun,name="register")
]