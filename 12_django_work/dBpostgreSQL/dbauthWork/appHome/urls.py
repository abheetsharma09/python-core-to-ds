from django.urls import path, include
from . import views

urlpatterns = [
    path('' , views.home , name ="home"),
     path('accounts/', include('allauth.urls')), 
    path('logout/' , views.logout_user , name="logout"),
    path('login/' , views.login_views , name="login"),
    path('signin/' , views.signin , name="signin"),
    path('dashboard/' , views.dashboard , name= "dashboard"),
    path('edit/<int:note_id>/', views.edit_note, name='edit_note'),
]

