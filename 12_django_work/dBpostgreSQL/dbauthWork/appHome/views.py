from django.shortcuts import render , redirect
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login
from django.contrib.auth import logout
from django.db import IntegrityError
from django.contrib import messages
from appHome.models import todoData

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
    if not requests.user.is_authenticated:
        return redirect('login') # Replace with your login URL pattern name

    if requests.method == "POST":   
        user_title = requests.POST.get("add_title")
        user_desc = requests.POST.get("add_desc")

        # Save to PostgreSQL
        todoData.objects.create(
            user=requests.user, 
            title=user_title,
            description=user_desc
        ) 
        
        # REDIRECT prevents duplicate data if the user hits refresh!
        return redirect('dashboard')

    # Fetch notes dynamically for the logged-in user
    user_notes = todoData.objects.filter(user=requests.user)
    return render(requests, 'dashboard.html', {'notes': user_notes})

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