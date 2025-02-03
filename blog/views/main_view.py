
from django.shortcuts import render

def home(request):
    return render(request,"main/home.html")

def create_blog(request):
    return render(request,"main/create_blog.html")

