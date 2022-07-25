from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import feature
from django.contrib.auth.models import User, auth
from django.contrib import messages



def index(request):
    features = Feature.objects.all()
    return render(request, 'index.html', {' features': features})


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already used')

    return render(request, 'register.html')

def index(request):
    return render (request,"index.html")

