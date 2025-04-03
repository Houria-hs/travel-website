from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.auth import logout , login 
from django.contrib.auth.forms import AuthenticationForm
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.contrib import messages
from .forms import RegisterForm , BookingForm
from .models import Destination , booking , Subscribe

# Create your views here.

def home(request):
    Destinations = Destination.objects.all()
    return render(request , 'home.html', {'Destinations': Destinations})

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
            messages.success(request , f'You are logged in {username}!')
            return redirect('home')
    else:
        loginForm= AuthenticationForm()
    return render(request , 'login.html' , {'loginForm':loginForm})

def logout_view(request):
    logout(request)
    return redirect('home')

def trip(request, pk):

    if not request.user.is_authenticated:
        messages.error(request, 'You are not authorized to access this page. Please log in!')
        return redirect('login')  

    trip = get_object_or_404(Destination, id=pk)  
    
    if request.method == 'POST':
        booking_form = BookingForm(request.POST)
        if booking_form.is_valid():
            booking = booking_form.save(commit=False)  
            booking.selected_trip = trip.title 
            booking.user = request.user  
            booking.save()  
            messages.success(request, 'Booking successful!')
            return redirect('home')
        else:
            messages.error(request, 'Correct the errors below!')

    else:
        booking_form = BookingForm()

    return render(request, 'trip.html', {'trip': trip, 'booking_form': booking_form})   

def Newsletter_view(request):
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        # Validate email format
        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, 'Invalid email format.')
            return redirect('home')
        
        if Subscribe.objects.filter(email = email).exists():
            messages.success(request , 'You are already saved')
            return redirect('home')
        else:
            Subscribe.objects.create(email = email)
            messages.success(request , 'Got it , thank you !')
    return render(request , 'home.html' , {})

