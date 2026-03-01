

# Create your views here.

from django.shortcuts import render
from .models import Event

def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

from django.shortcuts import get_object_or_404, redirect
from .models import Booking

def book_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        seats = request.POST.get("seats")

        Booking.objects.create(
            event=event,
            name=name,
            email=email,
            seats_booked=seats
        )
        return redirect("event_list")

    return render(request, "events/book_event.html", {"event": event})