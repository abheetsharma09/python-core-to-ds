from django.shortcuts import render , HttpResponse , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your views here.
def homePage(requests):
    if requests.user.isanonymous:
        redirect("/signIn")
    return render(requests , "home.html")

def signIn(requests):
    # return render(requests , 'signIn.html')
    return render(requests , "signIn.html")

def logIn(requests):
    if requests.method == "POST":
        username= requests.POST.get("username")
        password = requests.POST.get("password")

        user = authenticate(username=username, password=password)
        if user is not None:
        # A backend authenticated the credentials
            print("Correct Credentials")
            redirect("/")
        else:
        # No backend authenticated the credentials
            print("Wrong Credentials")

        # checks if the user enter correct credentials
    return render(requests, "login.html")