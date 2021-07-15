from django.shortcuts import render, redirect
from django.contrib import messages
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
        print(errors)
        return redirect('/contact')

    else:
        user = UserMessage.objects.create(
            username = request.POST['username'],
            email = request.POST['email'],
            message = request.POST['message']
        )
        ### Send an email
        send_mail(
           f'Message from {username}' , #subject
           "This is an automatic messager" , #message
            email , # from email
           ['marknovicio@gmail.com'] , # To Email
        )

        
        request.session['username'] = user.username
        request.session['email']= user.email
        request.session['message']= user.message
        return render(request, 'sent_email.html', {'username': username})

    



