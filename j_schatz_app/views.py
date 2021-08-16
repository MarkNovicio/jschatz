from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import *
from login_app.models import *

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

    if request.method == "POST":
        user = UserMessage.objects.create(
            username = request.POST['username'],
            email = request.POST['email'],
            message = request.POST['message']
        )
        ### Send an email
        send_mail(
            user.username , #subject
            user.message , #message
            user.email , # from email
            ['marknovicio@gmail.com'], # To Email
            fail_silently=False)

        
        request.session['username'] = user.username
        request.session['email']= user.email
        request.session['message']= user.message
        return render(request, 'sent_email.html', {'username': user.username})
    
def success_page(request):
    # if 'user_id' not in request.session:
    #     messages.error(request, "Please log in.")
    #     return redirect('/user/login')

    if 'user_id' in request.session:
        context = {
            "user": User.objects.get(id = request.session['user_id'])
        }

        return render(request, "success.html", context)
    else:
        return redirect('/user/registration') #login page

def post_challenge(request):
    errors = CodeChallenge.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
            print('pass')
            print(User.objects.get(id = request.session['user_id']))
        return redirect('/success')
    
    else:    
        CodeChallenge.objects.create(
        title = request.POST['title'],
        challenge_question = request.POST['challenge_question'],
        publisher = User.objects.get(id = request.session['user_id'])
        )

    return redirect('/post_challenge/challenges')

def challenge(request):     
    context = {
        "challenges": CodeChallenge.objects.all(),
        "user": User.objects.get(id = request.session['user_id'])
    }

    return render(request, 'challenges.html', context)

def coding_challenges(request, challenge_id):
    context = {
        "user": User.objects.get(id = request.session['user_id']),
        "challenge": CodeChallenge.objects.get(id=challenge_id)
    }

    return render(request, "coding_challenge.html", context)



