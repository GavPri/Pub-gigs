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


class Reservation(models.Model):
    reservation = models.BooleanField(default=False)
    gig = models.ForeignKey(Gig, on_delete=models.CASCADE)
    reserved_by = models.CharField(max_length=50)
    email_address = models.EmailField('Email Address', blank=True)
    age = models.IntegerField(default=16)
    num_of_guests = models.IntegerField(default=1)

    def __str__(self):
        return self.reserved_by
