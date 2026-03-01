

# Create your models here.
from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    total_seats = models.IntegerField()

    def __str__(self):
        return self.title
    
class Booking(models.Model):
    event = models.ForeignKey('Event', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    seats_booked = models.IntegerField()
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.event.title}"

    
   