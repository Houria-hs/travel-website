from django.db import models

# Create your models here.

class Destination(models.Model):
    title = models.CharField(max_length=200)
    price = models.TextField(max_length=20)
    days = models.CharField(max_length=10)
    people = models.CharField(max_length=10)
    image = models.ImageField(upload_to='destinations/')

    def __str__(self):
        return self.title