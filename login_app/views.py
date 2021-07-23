from django.shortcuts import render, redirect
from django.contrib import messages

from .models import User

def registration_form(request):

    return render(request, "sign_up.html")

def register_user(request):
    if request.method == 'GET':
        return redirect('/')
    errors = User.objects.basic_validator(request.POST)

    if len(errors) > 0:
        #This code should render the error messages in the
        # Registration section
        for key, value in errors.items():
            messages.error(request, value)
        print(errors)

        return redirect('/registration')
    
    else:
        # if the errors object is empty, that means there were no errors!
        # retrieve the blog to be updated, make the changes, and save
        print("user is good")
    
    return redirect('/')

