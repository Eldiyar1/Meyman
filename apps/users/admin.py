from django.contrib import admin

from .models import User, CarReservation, AccommodationReservation


admin.site.register(User)
admin.site.register(CarReservation)
admin.site.register(AccommodationReservation)
