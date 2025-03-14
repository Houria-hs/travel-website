from django.shortcuts import render , redirect
from django.contrib.auth import logout , login 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import RegisterForm

# Create your views here.

def home(request):
    return render(request , 'home.html' , {})



def Register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request , user)
            username = form.cleaned_data.get('username')
            messages.success(request , f'Account created for {username}!')
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request , 'register.html' , {'form': form})

def login_view(request):
    if request.method == 'POST':
        loginForm = AuthenticationForm(data = request.POST)
        if loginForm.is_valid():
            user = loginForm.get_user()
            login(request , user)
            username = loginForm.cleaned_data.get('username')
            messages.success(request , f'Account created for {username}!')
            return redirect('home')
    else:
        loginForm= AuthenticationForm()
    return render(request , 'login.html' , {'loginForm':loginForm})

def logout_view(request):
    logout(request)
    return redirect('home')
