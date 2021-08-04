from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
#from django.contrib.auth import views
import bcrypt



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
        pw_hash = bcrypt.hashpw(request.POST['password'].
        encode(), bcrypt.gensalt(rounds =13)).decode()
        print(pw_hash)
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
    signin_messages = messages
    try:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            #user = Users.objects.get(email = request.POST['email'])
            if not email or not password:
                messages.success(request, 'Both Username and Password are required.')
                return redirect('/login_page')
            user_email = User.objects.filter(email = email).first()
            if user_email is None:
                message.success(request, 'User not found.')
                return redirect('/login_page')
            
            user = authenticate(username = username, password = password)

            if user is None:
                message.success(request, "Wrong password")
                return redirect('/login_page')
            
            login(request, user)
            return redirect('/')
    
    except Exception as e:
        print(e)
    return render(request, 'login.html')


    # except:
    #     signin_messages.error(request, "Invalid email or password")
    #     return redirect('/login_page')
    
    # if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
    #     request.session['user_id'] = user.id
    #     request.session['first_name']= user.first_name
    #     request.session['last_name']=user.last_name
    #     request.session['email']= user.email
    #     return redirect('/')
    
    # signin_messages.error(request, "Incorrect email address or password.")
    # return redirect('/login_page')






