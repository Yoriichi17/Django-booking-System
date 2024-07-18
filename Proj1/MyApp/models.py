# MyApp/models.py

from django.db import models

class ComedyShowEvent(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=200)

class TicketBooking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    event = models.ForeignKey(ComedyShowEvent, on_delete=models.CASCADE)
    number_of_tickets = models.PositiveIntegerField()
