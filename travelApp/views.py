from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.auth import logout , login 
from django.contrib.auth.forms import AuthenticationForm
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.contrib import messages
from .forms import RegisterForm 
from .models import Destination , booking , Subscribe , PromoCode

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
        full_name = request.POST.get('FullName')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        numberOfTravelers = request.POST.get('numberOfTravelers')

        Booking = booking() 
        Booking.user_fullname = full_name
        Booking.user_email = email
        Booking.user_phone = phone
        Booking.number_of_travelers = numberOfTravelers
        Booking.selected_trip = trip.title
        Booking.user = request.user 
        Booking.save()
        messages.success(request, 'your informations has been saved successfuly !')
        return redirect('bookingSummary', trip_id=trip.id)
    
    return render(request, 'trip.html', {'trip': trip})   

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

def ThankYou(request):
    return render(request , 'ThankYou.html' , {})

def bookingSummary(request , trip_id):
    trip = get_object_or_404(Destination, id=trip_id)
    latest_booking = booking.objects.filter(selected_trip=trip).last()

    if not latest_booking:
        messages.error(request, "No booking found for this trip.")
        return redirect('trip', trip_id=trip_id)
    
    numberOfTravelers = latest_booking.number_of_travelers
    promoCodeInput = ''
    if request.method =='POST':
        promoCodeInput = request.POST.get('promo', '').strip()

    subtotal = float(trip.price_per_person )* numberOfTravelers
    discount = 0
    final_total = subtotal
    promo_error = None

    # Promo code logic
    if promoCodeInput:
        try:
            promo = PromoCode.objects.get(promo_code__iexact=promoCodeInput, is_active=True)
            discount = (promo.discount_percentage / 100) * subtotal
            final_total = subtotal - discount
        except PromoCode.DoesNotExist:
            promo_error = "Invalid promo code"

    context = {
        'trip': trip,
        'travelers': numberOfTravelers,
        'subtotal': subtotal,
        'discount': discount,
        'total': final_total,
        'promo_code': promoCodeInput,
        'promo_error': promo_error,
    }

    return render(request, 'bookingSummary.html', context)
