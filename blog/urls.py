from django.urls import path
from .views.main_view import home,create_blog
from .views.auth_view import register
from .views.auth_view import login




urlpatterns = [
   
    path("register/",register, name="register"),
    path("login/",login,name="login"),
  
     path('', home, name='home'),
    path('create/', create_blog, name='create_blog'),
]
