from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import *
from login_app.models import *

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def login(request):
    return render(request, "login.html")

def contact(request):
    if 'user_id' in request.session:
        context = {
            "user": User.objects.get(id = request.session['user_id'])
        }
    return render(request, "contact.html", context)

def submit_user_message(request):

    errors = UserMessage.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        print(errors)
        return redirect('/contact')

    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        message = request.POST['message']

        ### Send an email
        send_mail(
            username , #subject
            message , #message
            email, # from email
            ['th3arclearningcenter@gmail.com'], # To Email
            fail_silently=False
            )  
       ##request.session['username'] = user.username
        ##request.session['email']= user.email
       ## request.session['message']= user.message
        return render(request, 'sent_email.html', {'username': username})
    
def success_page(request):

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

def single_coding_challenge(request, challenge_id):
    context = {
        "challenge": CodeChallenge.objects.get(id=challenge_id)
    }

    return render(request, "coding_challenge.html", context)

def code_publisher(request, publisher_id):

    context = {
        "user": User.objects.get(id = publisher_id)
    }

    return render(request, "code_publisher.html", context)

def delete_challenge(request,challenge_id):
    del_challenge = CodeChallenge.objects.get(id=challenge_id)
    if del_challenge.publisher.id == request.session['user_id']:
        del_challenge.delete()
    return redirect('/post_challenge/challenges')

def update_user(request):
    user = User.objects.get(id = request.session['user_id'])
    errors = User.objects.edit_validator(request.POST, user)
    return redirect(f"/post_challenge/challenge_publisher/{request.session['user_id']}")
