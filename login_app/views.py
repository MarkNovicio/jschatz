from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages


def register_user(request):

    errors = User.objects.validator(request.POST)
    
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/user/registration')

    return redirect('/login')

    if request.method =="GET":
        return redirect('/')
# Create your views here.
