from django.contrib import admin

from .models import CarReservation, AccommodationReservation, CustomUser

admin.site.register(CustomUser)
admin.site.register(CarReservation)
admin.site.register(AccommodationReservation)
