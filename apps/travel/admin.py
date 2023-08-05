from django.contrib import admin
from .models import Hotel, Hostel, Apartment, GuestHouse, Sanatorium, Rating, HouseReservation, Room


class HousingAdmin(admin.ModelAdmin):
    list_display = ['housing_name', 'address', 'housing_type', 'accommodation_type', 'food_type']
    list_filter = ['housing_type']
    search_fields = ['housing_name']
    prepopulated_fields = {'slug': ('housing_name',)}


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    pass


@admin.register(HouseReservation)
class HouseReservationAdmin(admin.ModelAdmin):
    list_display = ('destination', 'check_in_date', 'check_out_date', 'adults', 'teens', 'children', 'infants', 'pets')
    list_filter = ('destination', 'check_in_date', 'check_out_date')
    search_fields = ('region',)


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('rating',)


@admin.register(Hotel)
class HotelAdmin(HousingAdmin):
    pass


@admin.register(Hostel)
class HostelAdmin(HousingAdmin):
    pass


@admin.register(Apartment)
class ApartmentAdmin(HousingAdmin):
    pass


@admin.register(GuestHouse)
class GuestHouseAdmin(HousingAdmin):
    pass


@admin.register(Sanatorium)
class SanatoriumAdmin(HousingAdmin):
    pass
