from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .forms import TaskForm
from .models import Todo

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
        
    
        if user is not None:
            login(request,user)
            return redirect("body")
    return render(request,"login.html")

def add_task(request):
    if request.method == "POST":
        form=TaskForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect("body")
    else:
        form=TaskForm()
    return render(request,"add_task.html",{'form':form})         
def body_fun(request):
    return render(request,"body.html")
def body1(request):
    print("Logged in user:", request.user)
    print("Is authenticated:", request.user.is_authenticated)

    tasks = Todo.objects.filter(user=request.user)

    print("Tasks:", tasks)
    print("Count:", tasks.count())

    return render(request, "body.html", {"tasks": tasks})

