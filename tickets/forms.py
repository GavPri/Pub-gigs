from django import forms
from django.forms import ModelForm
from .models import Booking


# Booking Form
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'email', 'age', 'tickets']