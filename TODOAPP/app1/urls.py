from django.contrib import admin
from django.urls import path,include
from app1 import views

urlpatterns = [
    path('',views.home_fun,name = "index"),
    path('Register/',views.register_fun,name="register"),
    path('login/',views.login_fun,name="login"),
    path('body/',views.body_fun,name="body"),
    path('add/',views.add_task,name="add_task"),
    path('complete/<int:task_id>/', views.complete_task, name="complete_task"),
    path('edit/<int:task_id>/', views.edit_task, name="edit_task"),
    path('delete/<int:task_id>/', views.delete_task, name="delete_task"),
]