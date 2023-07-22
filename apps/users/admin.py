from django.contrib import admin

from .models import Profile, Reservation, Favorite

admin.site.register(Profile)
admin.site.register(Reservation)
admin.site.register(Favorite)
