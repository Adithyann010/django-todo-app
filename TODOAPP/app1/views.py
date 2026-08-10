from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .forms import TaskForm
from .models import Todo
from django.shortcuts import get_object_or_404

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
    tasks = Todo.objects.filter(user=request.user)
    completed_count = tasks.filter(completed=True).count()
    pending_count = tasks.filter(completed=False).count()
    return render(request, "body.html", {
        "tasks": tasks,
        "completed_count": completed_count,
        "pending_count": pending_count,
    })
def complete_task(request, task_id):
    task = get_object_or_404(Todo, id=task_id, user=request.user)
    task.completed = True
    task.save()
    return redirect("body")


def delete_task(request, task_id):
    task = get_object_or_404(Todo, id=task_id, user=request.user)
    task.delete()
    return redirect("body")


def edit_task(request, task_id):
    task = get_object_or_404(Todo, id=task_id, user=request.user)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("body")
    else:
        form = TaskForm(instance=task)
    return render(request, "add_task.html", {"form": form})