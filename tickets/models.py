from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Gig(models.Model):
    band = models.CharField(max_length=50)
    time = models.TimeField()
    venue = models.CharField(max_length=200)
    date = models.DateField()
    featured_image = CloudinaryField('image', default='placeholder')

    def __str_(self):
        return f"{self.band} @ {self.venue}"
