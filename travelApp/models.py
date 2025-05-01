from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Destination(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200 , blank=True, null=True)
    price_per_person = models.CharField(max_length=20)
    days_and_nights = models.CharField(max_length=20)
    max_people = models.CharField(max_length=20)
    from_date = models.CharField(max_length = 20 , default='')
    To_date = models.CharField(max_length = 20 , default='')
    second_from_date = models.CharField(max_length = 20 , default='')
    second_To_date = models.CharField(max_length = 20 , default='')
    description = models.TextField(max_length = 1000 , default='')
    image = models.ImageField(upload_to='destinations/')
    tarif = models.TextField(max_length=1000 , blank=True, null=True)
    has_multiple_tarifs = models.BooleanField(default=False) 
    price_per_person = models.FloatField(blank=True, null=True) 
    is_available = models.BooleanField(default=True)


    def __str__(self):
        return self.title
    
class Tarif(models.Model):
    ROOM_CHOICES = [
        ('Double', 'Double'),
        ('Single', 'Single'),
        ('Enfant', 'Enfant'),
        ('CHD sans-lit', 'CHD sans-lit'),
        ('CHD avec-lit', 'CHD avec-lit'),
    ]

    destination = models.ForeignKey(Destination, related_name='tarifs', on_delete=models.CASCADE)
    room_type = models.CharField(max_length=20, choices=ROOM_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.destination.title} - {self.room_type.capitalize()} Room"

class booking(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Processing', 'Processing'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES,  default="Pending")
    user = models.ForeignKey(User , on_delete=models.CASCADE , null=True , blank= True)
    booking_date = models.DateTimeField(auto_now_add=True)
    user_fullname = models.CharField(max_length=200 , blank=True)
    user_phone = models.CharField(max_length = 10 , blank=True)
    user_email = models.EmailField(max_length=200 , blank=True)
    selected_trip = models.CharField(max_length=100)
    number_of_travelers = models.IntegerField()
    
    # NEW FIELDS:
    room_type = models.CharField(max_length=20, blank=True)
    room_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.user_fullname


class Subscribe(models.Model):
    email = models.EmailField(max_length=100 ,unique=True, blank=True)

    def __str__(self):
        return self.email
    

class PromoCode(models.Model):
    promo_code = models.CharField(max_length=20)
    discount_percentage = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.promo_code

class PayementProof(models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    trip_title = models.CharField(max_length=100)
    transfer_date = models.DateField()
    screenshot = models.ImageField(upload_to="paymentProofs/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name