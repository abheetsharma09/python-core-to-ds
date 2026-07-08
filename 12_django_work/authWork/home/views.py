from django.shortcuts import render , HttpResponse , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , logout , login
from django.contrib import messages

# Create your views here.
def homePage(requests):
    if requests.user.is_authenticated:
        return render(requests , "home.html")
    else:
        return redirect("login/")
        

def signIn(requests):
    if requests.user.is_authenticated:
        return redirect("/")
    
    if requests.method == "POST":
        u_name = requests.POST.get("name")
        u_username = requests.POST.get("username")
        u_email = requests.POST.get("email")
        u_password = requests.POST.get("password")
        u_password_check = requests.POST.get("password-check")

        if u_password != u_password_check:
            messages.add_message(requests, messages.INFO, "Password does not match")
            messages.add_message(requests, messages.INFO, "Retype Password")
            return render(requests , "signIn.html")

        if User.objects.filter(username=u_username).exists():
            messages.add_message(requests, messages.INFO, "User already exists!!")
            return redirect('/login')

        user = User.objects.create_user(username=u_name, email=u_email, password=u_password)
        user.first_name = u_name
        user.save()

        login(requests, user)

        return redirect("/")

    return render(requests , "signIn.html")

def logIn(requests):
    if requests.user.is_authenticated:
        return redirect("/")
    
    if requests.method == "POST":
        username= requests.POST.get("username")
        password = requests.POST.get("password")

        user = authenticate(username=username, password=password)
        if user is not None:
        # A backend authenticated the credentials
            login(requests, user) 
            messages.add_message(requests, messages.INFO, f"Welcome Back {username}")
            return redirect("/")
        else:
        # No backend authenticated the credentials
            messages.add_message(requests, messages.INFO, "Wrong Credentials..Try Again")
            messages.add_message(requests, messages.INFO, "Click Forget Password??..")

        # checks if the user enter correct credentials
    return render(requests, "login.html")

def logout_user(requests):
    logout(requests)
    messages.add_message(requests , messages.INFO , "Logout Sucessfull !!")
    return redirect('/login')