from django.contrib import admin

from .models import Profile, CarReservation, AccommodationReservation

admin.site.register(Profile)
admin.site.register(CarReservation)
admin.site.register(AccommodationReservation)
