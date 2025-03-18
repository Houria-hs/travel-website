from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Destination(models.Model):
    title = models.CharField(max_length=200)
    price = models.TextField(max_length=20)
    days = models.CharField(max_length=10)
    people = models.CharField(max_length=10)
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