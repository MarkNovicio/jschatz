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
    # try:
    #     if request.method == "POST":
    #         email = request.POST.get('email')
    #         password = request.POST.get('password')    

    #         if not username or not password:
    #             messages.error(request, "Invalid email or password!!!!")   
    #             return redirect('/login_page')

    #         user_obj = User.objects.filter(username = username).first()
    #         if user_obj is None:
    #             messages.error(request, "User not found")   
    #             return redirect('/login_page')
            
    #         user = authenticate(email = email, password = password)

    #         if user is None:
    #             messages.error(request, "Wrong password")   
    #             return redirect('/login_page')
    #         login(request, user)
    #         return redirect('/success')
    # except Exception as e:
    #     print(e)
    # return render(request, 'login')
    try:
        user = User.objects.get(email = request.POST['email'])
        
    except:
        messages.error(request, "Invalid email or password!!!!")
        return redirect('/login_page')
    
    if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
        print(request.POST['password'])
        logged_users = User.objects.filter(email=request.POST['email'])
        user_login_success = logged_users[0]
        print(user_login_success)
        return redirect('/success')
    
    messages.error(request, "Incorrect email address or passworddddddd.")
    return redirect('/login_page')






