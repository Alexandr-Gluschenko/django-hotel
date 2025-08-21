from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from datetime import date


class RoomType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Room(models.Model):
    number = models.IntegerField()
    room_type = models.ForeignKey('RoomType', on_delete=models.CASCADE, related_name='rooms')
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Room {self.number} - {self.room_type.name}"

class Guest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} ({self.email})"

class Booking(models.Model):
    check_in = models.DateField()
    check_out = models.DateField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='bookings')
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE, related_name='bookings')
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2, editable=False)

    def clean(self):
        if self.check_out <= self.check_in:
            raise ValidationError("The check-in date must be before the check-out date.")

        overlapping_bookings = Booking.objects.filter(
            room=self.room,
            check_in__lt=self.check_out,
            check_out__gt=self.check_in,
        )
        if self.pk:
            overlapping_bookings = overlapping_bookings.exclude(pk=self.pk)

        if overlapping_bookings.exists():
            raise ValidationError("The room is already booked for these dates.")

    def save(self, *args, **kwargs):
        if not self.pk:
            self.price_per_night = self.room.price_per_night
        super().save(*args, **kwargs)

    def total_price(self):
        nights = (self.check_out - self.check_in).days
        return nights * self.price_per_night

    def __str__(self):
        return f"Booking for {self.guest.name} in Room {self.room.number}"
