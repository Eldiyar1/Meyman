from django.contrib import admin
from .models import Hotel, Hostel, Apartment, Sanatorium, HousingReview, HousingReservation, Room, House, HousingImage, \
    RoomImage


class HousingImageInline(admin.TabularInline):
    model = HousingImage
    min_num = 5
    max_num = 20
    extra = 0


class HousingAdmin(admin.ModelAdmin):
    list_display = ('housing_name', 'address', 'housing_type', 'accommodation_type', 'food_type')
    list_filter = ('housing_type', 'region', 'stars', 'food_type')
    search_fields = ('housing_name', 'address')
    prepopulated_fields = {'slug': ('housing_name',)}
    inlines = (HousingImageInline,)


@admin.register(HousingReservation)
class HousingReservationAdmin(admin.ModelAdmin):
    list_display = ('user', 'housing', 'check_in_date', 'check_out_date', 'get_total_guests', 'pets')
    list_filter = ('destination', 'check_in_date', 'check_out_date')
    search_fields = ('user__username', 'housing__housing_name')

    def get_total_guests(self, obj):
        return obj.adults + obj.teens + obj.children + obj.infants

    get_total_guests.short_description = 'Total Guests'


@admin.register(HousingReview)
class HousingReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'housing', 'overall_experience', 'staff_rating', 'comfort_rating', 'cleanliness_rating',
                    'value_for_money_rating', 'food_rating', 'location_rating')
    list_filter = ('overall_experience', 'staff_rating', 'comfort_rating', 'cleanliness_rating',
                   'value_for_money_rating', 'food_rating', 'location_rating')
    search_fields = ('user__username', 'housing__housing_name')


class RoomImageInline(admin.TabularInline):
    model = RoomImage
    min_num = 5
    max_num = 20
    extra = 0


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('housing', 'room_name', 'price_per_night', 'max_guest_capacity', 'room_area')
    list_filter = ('housing', 'room_name', 'smoking_allowed', 'without_card', 'free_cancellation')
    search_fields = ('housing__housing_name', 'room_name')
    inlines = (RoomImageInline,)


@admin.register(Hotel)
class HotelAdmin(HousingAdmin):
    pass


@admin.register(Hostel)
class HostelAdmin(HousingAdmin):
    pass


@admin.register(Apartment)
class ApartmentAdmin(HousingAdmin):
    pass


@admin.register(House)
class HouseAdmin(HousingAdmin):
    pass


@admin.register(Sanatorium)
class SanatoriumAdmin(HousingAdmin):
    pass
