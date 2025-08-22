from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from home.models import Booking


# Create your views here.
def index(request):
    return render(request, "home/index.html")


class BookingListView(ListView):
    model = Booking
    template_name = 'home/booking_list.html'
    context_object_name = 'bookings'

class BookingDetailView(DetailView):
    model = Booking
    template_name = 'home/booking_detail.html'
    context_object_name = 'booking'

class BookingCreateView(CreateView):
    model = Booking
    template_name = "home/booking_create.html"
    fields = ['check_in', 'check_out', 'guest_count', 'rooms_count', 'phone']
    success_url = reverse_lazy('home:booking_list')

