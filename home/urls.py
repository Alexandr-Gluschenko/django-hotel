from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

from .views import BookingListView, BookingDetailView, BookingCreateView

app_name = "home"

urlpatterns = [
    path('', views.index, name='index'),
    path('bookings/', BookingListView.as_view(), name='booking_list'),
    path('bookings/<int:pk>/', BookingDetailView.as_view(), name='booking_detail'),
    path('bookings/create/', BookingCreateView.as_view(), name='booking_create'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home:login'), name='logout'),
]
