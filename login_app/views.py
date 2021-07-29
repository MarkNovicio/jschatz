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

def login_page(request):
    return render(request, "login.html")

def login(request):
    signin_messages = messages
    if request.method == "GET":
        return redirect('/')
    if not User.objects.basic_validator(request.POST['email'], request.POST['password']):
        signin_messages.error(request, 'Invalid email/password')
        return redirect('/user/signup')
    
    else:
        logged_users = User.objects.filter(email=request.POST['email'])
        user = logged_users[0]
        request.session['user_id'] = user.id
        request.session['first_name']= user.first_name
        request.session['last_name']=user.last_name
        request.session['email']= user.email
        return redirect('/user/signup')
    
def forgot_password_page(request):
    return render(request, "forgot_password.html")
    


