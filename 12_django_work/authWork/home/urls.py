from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("" , views.homePage , name="homePage"),
    path("signIn/" , views.signIn , name="signIn"),
    path("login/" , views.logIn , name="logIn"),
    path("logout/" , views.logout_user, name="logout"),
    path("dashboard/" , views.dashboard, name="dashboard")
]