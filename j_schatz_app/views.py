from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import *

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    
    return render(request, "contact.html")

def submit_user_message(request):
    errors = UserMessage.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
            
    print(request.POST)
    return redirect('/')
    



