from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def home_fun(request):
    return render(request,"index.html")

def register_fun(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        confirm_password=request.POST.get("confirm_password")
        
        if (password != confirm_password):
            return render(request,"register.html",{"error": "the password does'nt match the confirm password"})
        
        if User.objects.filter(username=username).exists():
            return render(request,"register.html",{"error": "the username is already taken"})
        User.objects.create_user(
            username = username,
            email = email,
            password = password
        )
        return redirect("login")

            
    return render(request,"register.html")

def login_fun(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
    
        user = authenticate(request,
                            username=username,
                            password=password)
    return render(request,"login.html")


