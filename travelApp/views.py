from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.auth import logout , login 
from django.contrib.auth.forms import AuthenticationForm
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.contrib import messages
from .forms import RegisterForm  , CustomLoginForm
from .models import Destination ,Booking , Subscribe , PromoCode , PayementProof , Tarif

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
            messages.success(request , f'Compte créé pour {username}!')
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request , 'register.html' , {'form': form})

def login_view(request):
    if request.method == 'POST':
        loginForm = CustomLoginForm(data = request.POST)
        if loginForm.is_valid():
            user = loginForm.get_user()
            login(request , user)
            username = loginForm.cleaned_data.get('username')
            messages.success(request , f'Vous êtes connecté(e), {username}!')
            return redirect('home')
    else:
        loginForm= CustomLoginForm()
    return render(request , 'login.html' , {'loginForm':loginForm})

def logout_view(request):
    logout(request)
    return redirect('home')

from django.core.exceptions import ObjectDoesNotExist

def trip(request, pk):
    if not request.user.is_authenticated:
        messages.error(request, 'Vous n’êtes pas autorisé(e) à accéder à cette page. Veuillez vous connecter !')
        return redirect('login')  

    trip = get_object_or_404(Destination, id=pk)  
    tarifs = Tarif.objects.filter(destination=trip)
    
    if request.method == 'POST':
        full_name = request.POST.get('FullName')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        numberOfTravelers = request.POST.get('numberOfTravelers')
        room_type = request.POST.get('roomType')

        booking = Booking() 
        booking.user_fullname = full_name
        booking.user_email = email
        booking.user_phone = phone
        booking.number_of_travelers = numberOfTravelers
        booking.selected_trip = trip.title
        booking.user = request.user 

        try:
            if trip.has_multiple_tarifs:
                tarif = Tarif.objects.get(destination=trip, room_type=room_type)
                booking.room_type = room_type
                booking.room_price = float(tarif.price) 
            else:
                booking.room_type = "Standard"
                booking.room_price = trip.price_per_person

            booking.save()
            messages.success(request, 'Vos informations ont été enregistrées avec succès !')
            return redirect('bookingSummary', trip_id=trip.id)

        except ObjectDoesNotExist:
            messages.error(request, "Erreur : Tarif introuvable pour ce type de chambre.")
            return redirect('trip', pk=trip.id)

    return render(request, 'trip.html', {'trip': trip, 'tarifs': tarifs})


def Newsletter_view(request):
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        # Validate email format
        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, ' Format d’e-mail invalide.')
            return redirect('home')
        
        if Subscribe.objects.filter(email = email).exists():
            messages.success(request , 'Vous êtes déjà enregistré(e).')
            return redirect('home')
        else:
            Subscribe.objects.create(email = email)
            messages.success(request , ' Compris, merci !')
    return render(request , 'home.html' , {})

def ThankYou(request):
    return render(request , 'ThankYou.html' , {})

def bookingSummary(request , trip_id):
    trip = get_object_or_404(Destination, id=trip_id)
    latest_booking = Booking.objects.filter(selected_trip=trip).last()

    if not latest_booking:
        messages.error(request, "Aucune réservation trouvée.")
        return redirect('trip', trip_id=trip_id)

    numberOfTravelers = latest_booking.number_of_travelers
    promoCodeInput = ''
    if request.method =='POST':
        promoCodeInput = request.POST.get('promo', '').strip()


    if trip.has_multiple_tarifs:
        price_per_person = latest_booking.room_price
    else:
        price_per_person = trip.price_per_person

    subtotal = float(price_per_person )* numberOfTravelers
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
        'price_per_person': price_per_person,
    }
    return render(request, 'bookingSummary.html', context)

def payement_view(request):
    return render(request , 'Payement.html' , {})