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


class GuestList(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    gig = models.ForeignKey(Gig, on_delete=models.CASCADE)
