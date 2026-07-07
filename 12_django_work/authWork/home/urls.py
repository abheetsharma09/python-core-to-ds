from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("" , views.homePage , name="homePage"),
    path("signIn/" , views.signIn , name="signIn"),
    path("logIn/" , views.logIn , name="logIn")
]