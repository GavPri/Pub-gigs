from django import forms
from django.forms import ModelForm
from .models import Reservation


# Reservation Form
class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = "__all__"
