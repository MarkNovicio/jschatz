from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

def index(request):

    return render(request, "index.html")

def register_user(request):
    print("works")
    errors = User.objects.validator(request.POST)
    
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/user/registration')
    
    else:
        # if the errors object is empty, that means there were no errors!
        # retrieve the blog to be updated, make the changes, and save
        user = User.objects.get(id = id)
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.password = request.POST['password']
        user.save()
        messages.success(request, "Blog successfully updated")
        # redirect to a success route
        return redirect('/')

