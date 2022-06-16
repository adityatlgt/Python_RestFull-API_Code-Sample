from django.db import models
from django.utils import timezone

# Create your models here.

class Screens(models.Model):
    "to save details of available shows"
    multiplex = models.CharField(max_length=255)
    movie_name = models.CharField(max_length=255)
    cast = models.CharField(max_length=255)
    description = models.TextField()
    show_timing = models.DateTimeField()
    city = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(null=True, blank=True)


class Bookings(models.Model):
    "to save bookings made by the customers"
    booking_id = models.CharField(max_length=255)
    user = models.CharField(max_length=255)
    time_booked = models.DateTimeField(default=timezone.now)
    email = models.EmailField()
    mobile = models.CharField(max_length=255)
    show_booked = models.ForeignKey(Screens, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(null=True, blank=True)    
