from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Gig(models.Model):
    band = models.CharField(max_length=50)
    time = models.TimeField()
    venue = models.CharField(max_length=200)
    date = models.DateField()
    featured_image = CloudinaryField('image', default='placeholder')
    bookings = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.venue


class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.PositiveIntegerField()
    tickets = models.PositiveIntegerField()

    def __str__(self):
        return f"Booking by {self.name}"
