from django.shortcuts import render, redirect
from django.contrib.auth.models import User


def index(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'pages/index.html')
