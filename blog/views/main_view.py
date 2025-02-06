from django.shortcuts import render, redirect
from ..models import Blog
from django.contrib.auth.decorators import login_required

 
def home(request):
    return render(request, "main/home.html")


#yesle login required garna help garcha

@login_required
def create_blog(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        content = request.POST.get("content")
        publisher = request.POST.get("publisher")
        image = request.FILES.get("image")

        blog = Blog(title=title, author=author, content=content, publisher=publisher,image=image)
        blog.save()

        # Redirect to the home page or a blog list page after saving
        return redirect('home')  # Make sure you have a URL named 'home'

    return render(request, "main/create_blog.html")
