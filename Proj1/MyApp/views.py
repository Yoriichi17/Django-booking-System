# MyApp/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import ComedyShowEvent, TicketBooking
from .forms import TicketBookingForm

def index(request):
    events = ComedyShowEvent.objects.all()
    return render(request, 'MyApp/index.html', {'events': events})

def book_ticket(request, event_id):
    event = get_object_or_404(ComedyShowEvent, pk=event_id)
    if request.method == 'POST':
        form = TicketBookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.event = event
            booking.save()
            return redirect('booking_confirmation')
    else:
        form = TicketBookingForm()
    return render(request, 'MyApp/book_ticket.html', {'form': form, 'event': event})

def booking_confirmation(request):
    bookings = TicketBooking.objects.all()
    return render(request, 'MyApp/booking_confirmation.html', {'bookings': bookings})
