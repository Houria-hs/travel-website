from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Destination(models.Model):
    title = models.CharField(max_length=200)
    price_per_person = models.TextField(max_length=20)
    days_and_nights = models.CharField(max_length=10)
    max_people = models.CharField(max_length=10)
    from_date = models.CharField(max_length = 20 , default='')
    To_date = models.CharField(max_length = 20 , default='')
    second_from_date = models.CharField(max_length = 20 , default='')
    second_To_date = models.CharField(max_length = 20 , default='')
    description = models.CharField(max_length = 1000 , default='')
    image = models.ImageField(upload_to='destinations/')

    def __str__(self):
        return self.title
    

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
