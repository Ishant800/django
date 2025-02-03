from django.urls import path
from .views.main_view import home,create_blog
from .views.auth_view import register
from .views.auth_view import login




urlpatterns = [
    path("",home),
    path("register/",register),
    path("login/",login),
    path("create",create_blog)
]
