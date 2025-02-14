from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author= models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images',blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
class Register(models.Model):
    fullName = models.CharField(max_length=100)
    emailAddress = models.CharField(max_length=200)
    password = models.CharField(max_length=100)
    regesiter_at = models.DateTimeField(auto_now_add=True)
    
    