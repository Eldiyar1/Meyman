from django.contrib import admin
from .models import PriceRange, HousingType, AccommodationType, BedType, TravelService, Hotel, Hostel, \
    Apartment, GuestHouse, News, Author


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
    search_fields = ['accommodation_name']


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


@admin.register(TravelService)
class TravelServiceAdmin(admin.ModelAdmin):
    list_display = ['service_name', 'price', 'location', 'start_date', 'end_date', 'is_available']
    list_filter = ['is_available', 'start_date', 'end_date']
    search_fields = ['service_name']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['fullname']


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'formatted_published_date']
    list_filter = ['published_date']
    search_fields = ['title', 'author__username']

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['published_date']
        return []
