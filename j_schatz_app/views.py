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
    if request.method == "GET":
        return redirect('/')
    



