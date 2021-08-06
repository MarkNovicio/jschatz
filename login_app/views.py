from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
#from django.contrib.auth import views
import bcrypt



def registration_form(request):

    return render(request, "sign_up.html")

def register_user(request):
    errors = User.objects.basic_validator(request.POST)

    if request.method == 'GET':
        return redirect('/')   

    if len(errors) > 0:
        #This code should render the error messages in the
        # Registration section
        for key, value in errors.items():
            messages.error(request, value)
        print(errors)

        return redirect('/registration')
    
    else:
        pw_hash = bcrypt.hashpw(request.POST['password'].
        encode(), bcrypt.gensalt(rounds =13)).decode()
        User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            password = pw_hash
        )
        # if the errors object is empty, that means there were no errors!
        # retrieve the blog to be updated, make the changes, and save
  
    return redirect('/')

def login_page(request):
    return render(request, "login.html")

def login(request):
    try:
        user = User.objects.get(email = request.POST['email'])
        
    except:
        messages.error(request, "Invalid email or password!!!!")
        return redirect('/login_page')
    
    if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
        logged_users = User.objects.filter(email=request.POST['email'])
        user_login_success = logged_users[0]
        print(user_login_success)
        request.session['user_id'] = user.id
        request.session['first_name']= user.first_name
        request.session['last_name']=user.last_name
        request.session['email']= user.email
        return redirect('/success')
    
    messages.error(request, "Incorrect email address or passworddddddd.")
    return redirect('/login_page')



def logout(request):
    if "user_id" in request.session:
        del request.session['user_id']
    if "first_name" in request.session:
        del request.session['first_name']
    if "last_name" in request.session:
        del request.session['last_name']
    if "email" in request.session:
        del request.session['email']
    return redirect('/')



