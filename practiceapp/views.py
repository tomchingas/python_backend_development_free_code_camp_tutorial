from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature     # import Feature model from models.py

# Create your views here.
# defines function to return http response
def index(request):
    features = Feature.objects.all() # assigns Feature model to features object
    return render(request, 'index.html', {'features': features}) # middle references the index.html file, last part references the features list

# function to create user registration
def register(request):
    if request.method == 'POST': # if this request is being sent by POST then we want to capture all of this info
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_check = request.POST['password_check']

        if password == password_check:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Used')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request,'Password Not The Same')
            return redirect('register')
    else:   
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username =request.POST['username']
        password =request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None: # checks if user is registered on platform
            auth.login(request, user)   # logs in user
            return redirect('/')    #redirects to home page
        else:
            messages.info(request, 'Credentials Invalid')   
            return redirect('login')

    else:
        return render (request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def counter(request):
    text = request.POST['text'] # uses csrf token 
    amount_of_words = len(text.split())
    return render(request, 'counter.html', {'amount': amount_of_words})