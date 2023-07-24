from django.shortcuts import render
from django.views import generic
from .models import Gig, Reservation
from .forms import ReservationForm


class GigList(generic.ListView):
    model = Gig
    queryset = Gig.objects.all()
    template_name = 'index.html'
    paginate_by = 6


class ReservationList(generic.FormView):
    form_class = ReservationForm
    model = Reservation
    template_name = 'reservations.html'
