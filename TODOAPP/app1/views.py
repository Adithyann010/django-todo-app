from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_fun(request):
    return render(request,"index.html")
def register_fun(request):
    return render(request,"register.html")
def login_fun(request):
    return render(request,"login.html")

