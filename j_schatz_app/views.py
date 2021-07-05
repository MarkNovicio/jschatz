from django.shortcuts import render
from django.cor.mail import send_mail


def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    if request.method == "POST":
        
    return render(request, "contact.html")


