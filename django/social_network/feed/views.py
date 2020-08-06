from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Post


@login_required
def feed(request):
    if request.user.is_authenticated:
        # Get the users name
        user = request.user.username

        posts = Post.objects.order_by("-published_date")

        context = {
            "username": user,
            "posts": posts
        }
        return render(request, "feed/feed.html", context)
    else:
        return redirect("login")


@login_required
def post(request):
    if request.method == "POST":
        content = request.POST["content"]
        user = request.user

        post = Post(author=user, content=content)
        post.save()

    return redirect("feed")
