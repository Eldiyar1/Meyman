from django.contrib import admin

from .models import Profile, CarReservation, AccommodationReservation, AdminReview

admin.site.register(Profile)
admin.site.register(CarReservation)
admin.site.register(AccommodationReservation)
admin.site.register(AdminReview)
