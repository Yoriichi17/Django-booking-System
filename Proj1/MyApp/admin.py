# MyApp/admin.py

from django.contrib import admin
from .models import ComedyShowEvent, TicketBooking

class ComedyShowEventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'time')
    list_filter = ('date',)

class TicketBookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'number_of_tickets', 'event')
    list_filter = ('event',)

admin.site.register(ComedyShowEvent, ComedyShowEventAdmin)
admin.site.register(TicketBooking, TicketBookingAdmin)
