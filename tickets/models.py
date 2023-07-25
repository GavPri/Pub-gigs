from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Gig(models.Model):
    band = models.CharField(max_length=50)
    time = models.TimeField()
    venue = models.CharField(max_length=200)
    date = models.DateField()
    featured_image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.venue


# Guest List Model
class GuestList(models.Model):
    gig = models.ForeignKey(Gig, on_delete=models.CASCADE)
    guest_name = models.CharField(max_length=100)
    num_tickets = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.guest_name} - {self.num_tickets} tickets"
