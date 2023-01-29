from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [
    {
        "author": "Manu Labricole",
        "title": "Blog Post 1",
        "content": "first post content",
        "date_posted": "Jan 29, 2023"
    },
    {
        "author": "Per Wing",
        "title": "Blog Post PerBoy",
        "content": "Per first post content",
        "date_posted": "Jan 31, 2023"
    },
]


def home(request):
    context = {
        "posts": posts
    }

    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html")
