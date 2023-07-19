from django.contrib import admin
from .models import PriceRange, HousingType, AccommodationType, BedType, Hotel, Hostel, Apartment, GuestHouse


@admin.register(PriceRange)
class PriceRangeAdmin(admin.ModelAdmin):
    pass


@admin.register(HousingType)
class HousingTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(AccommodationType)
class AccommodationTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(BedType)
class BedTypeAdmin(admin.ModelAdmin):
    pass


class HousingAdmin(admin.ModelAdmin):
    list_display = ['housing_name', 'daily_price', 'available_rooms', 'is_available', 'location']
    list_filter = ['is_available', 'housing_type']
    search_fields = ['housing_name']


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

