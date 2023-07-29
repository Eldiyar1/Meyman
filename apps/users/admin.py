from django.contrib import admin

from .models import CarReservation, AccommodationReservation, CustomUser, User,Role

admin.site.register(User)
admin.site.register(CarReservation)
admin.site.register(AccommodationReservation)
admin.site.register(CustomUser)
admin.site.register(Role)