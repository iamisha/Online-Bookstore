from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def home(request):
    book = Book.objects.all()


    context = {
        'book':book,
    }
    return render(request, 'home.html', context)

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username = request.POST['username'], password = request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html',{'error: Username or Password is incorrect!'})
        
    else:
        return render(request, 'login.html')
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'signup.html', {'error': "Username is already taken"})
            
            except User.DoesNotExist:
                first_name = request.POST['first_name']
                last_name = request.POST['last_name']
                user = User.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password1'],
                    first_name=first_name,
                    last_name=last_name
                )
                auth.login(request, user)
                return redirect('home')  
    return render(request, 'signup.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
