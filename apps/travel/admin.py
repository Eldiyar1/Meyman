from django.contrib import admin
from .models import Hotel, Hostel, Apartment, GuestHouse, HousingAmenities, RoomAmenities, Sanatorium


class HousingAmenitiesInline(admin.TabularInline):
    model = HousingAmenities
    pass


class RoomAmenitiesInline(admin.TabularInline):
    model = RoomAmenities
    pass


class HousingAdmin(admin.ModelAdmin):

    list_display = ['housing_name', 'location', 'price_per_night', 'housing_type', 'accommodation_type',
    'bed_type', 'food_type']
    list_filter = ['housing_type']
    search_fields = ['housing_name']


@admin.register(Hotel)
class HotelAdmin(HousingAdmin):
    inlines = [HousingAmenitiesInline, RoomAmenitiesInline]


@admin.register(Hostel)
class HostelAdmin(HousingAdmin):
    inlines = [HousingAmenitiesInline, RoomAmenitiesInline]


@admin.register(Apartment)
class ApartmentAdmin(HousingAdmin):
    inlines = [HousingAmenitiesInline, RoomAmenitiesInline]


@admin.register(GuestHouse)
class GuestHouseAdmin(HousingAdmin):
    inlines = [HousingAmenitiesInline, RoomAmenitiesInline]


@admin.register(Sanatorium)
class SanatoriumAdmin(HousingAdmin):
    inlines = [HousingAmenitiesInline, RoomAmenitiesInline]
