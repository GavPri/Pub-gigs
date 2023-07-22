from django.shortcuts import render
from django.views import generic
from .models import Gig

class GigList(generic.ListView):
    model = Gig
    queryset = Gig.objects.all
    template_name = 'index.html'
    paginate_by = 6

