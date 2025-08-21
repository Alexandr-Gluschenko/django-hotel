from django.shortcuts import render
from django.views.generic import ListView, DetailView

from home.models import Booking


# Create your views here.
def index(request):
    return render(request, "home/index.html")


class BookingListView(ListView):
    model = Booking
    template_name = 'hotel/booking_list.html'
    context_object_name = 'bookings'

class BookingDetailView(DetailView):
    model = Booking
    template_name = 'hotel/booking_detail.html'
    context_object_name = 'booking'