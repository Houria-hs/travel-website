from django import forms
from django.contrib.auth.models import User 
from .models import booking
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    gender = forms.CharField(required=False , widget=forms.widgets.TextInput(attrs={"placeholder": "woman/man"}))
    age = forms.CharField(required=True , widget=forms.widgets.NumberInput(attrs={"placeholder": "18"}))

    class Meta:
        model = User
        fields = { 'password1' ,'password2', 'username' ,'gender' , 'age','email' }


class BookingForm(forms.ModelForm):
    fullname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}))
    number_of_travelers = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))

    class Meta:
        model = booking
        fields = ['fullname', 'email', 'phone', 'number_of_travelers']