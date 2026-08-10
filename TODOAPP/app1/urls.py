from django.contrib import admin
from django.urls import path,include
from app1 import views

urlpatterns = [
    path('',views.home_fun,name = "index"),
    path('Register/',views.register_fun,name="register"),
    path('login/',views.login_fun,name="login"),
    path('body/',views.body_fun,name="body"),
    path('body1/',views.body1,name="body1"),
    path('add/',views.add_task,name="add_task")
]