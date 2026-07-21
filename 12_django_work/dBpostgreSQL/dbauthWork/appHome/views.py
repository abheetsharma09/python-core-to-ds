from django.shortcuts import render , redirect
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login
from django.contrib.auth import logout
from django.db import IntegrityError
from django.contrib import messages

# Create your views here.
def home(requests):
    context = {
        'currDate' : datetime.today(),
    }
    return render(requests , 'landing.html' , context)

def logout_user(requests):
    logout(requests)
    return redirect('login')

def dashboard(requests):
    if requests.user.is_authenticated:
        return render(requests , 'dashboard.html')
    else:
        return redirect('')

def signin(requests):
    if requests.user.is_authenticated:
        return render(requests , 'dashboard.html')
    else:
        if requests.method == "POST":
            u_username = requests.POST.get("username")
            u_email = requests.POST.get("email")
            u_password =requests.POST.get("password")

            try:
                new_user =  User.objects.create_user(
                    username = u_username,
                    email = u_email,
                    password = u_password
                )
                login(
                    requests,
                    new_user, 
                    backend='django.contrib.auth.backends.ModelBackend'
                )

                return redirect('dashboard')
            except IntegrityError:
                return render(requests, 'signin.html', {'error_msg': 'That username/email is already taken!'})

        return render(requests ,'signin.html')

def login_views(requests):
    if requests.user.is_authenticated:
        return redirect("dashboard")
    
    if requests.method == "POST":
        u_username = requests.POST.get("username")
        u_password =requests.POST.get("password")

        user = authenticate(username=u_username, password=u_password)

        if user is not None:
        # A backend authenticated the credentials
            login(
                requests, 
                user,
                backend='django.contrib.auth.backends.ModelBackend'
                ) 
            return redirect('dashboard')
        else:
        # No backend authenticated the credentials
            return redirect('home')

    
    return render(requests ,'login.html')