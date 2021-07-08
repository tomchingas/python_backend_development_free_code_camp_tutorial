from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),    # makes default web address (the first input '') reference the index function from views.py
    path('counter', views.counter, name='counter'),
    path('register', views.register, name='register'),   # makes /register webaddress for user authentication
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    ]