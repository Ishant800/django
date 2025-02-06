from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.hashers import make_password

def register(request):
    if request.method == "POST":
        full_name = request.POST.get("fullName")
        email = request.POST.get("emailAddress")
        password = request.POST.get("password")

        if User.objects.filter(username=email).exists():
            return render(request, "auth/register.html", {"error": "Email already registered!"})

        user = User.objects.create(
            username=email, 
            first_name=full_name,
            email=email,
            password=make_password(password)  # Hash the password
        )
        
        return redirect("login")    
                
    return render(request, "auth/register.html")


def login(request):
    if request.method == 'POST':
        email = request.POST.get("emailAddress")
        password = request.POST.get("password")

        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            auth_login(request, user)  # Use Django's login function
            return redirect("home")
        else:
            return render(request, "auth/login.html", {"error": "Invalid email or password!"})

    return render(request, "auth/login.html")


def logout_view(request):
    logout(request)
    return redirect("login")
