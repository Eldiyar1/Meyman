from django import forms
from django.contrib import admin
from .models import Hotel, Hostel, Apartment, GuestHouse, Sanatorium, Rating, HouseReservation, Room, Housing, \
    HousingImage, RoomImage
from multiupload.fields import MultiFileField


class HousingImageForm(forms.ModelForm):
    class Meta:
        model = HousingImage
        fields = '__all__'

    images = MultiFileField(min_num=5, max_num=20, max_file_size=1024 * 1024 * 5)


class HousingImageInline(admin.TabularInline):
    model = HousingImage
    form = HousingImageForm
    extra = 1


class HousingAdmin(admin.ModelAdmin):
    list_display = ['housing_name', 'address', 'housing_type', 'accommodation_type', 'food_type']
    list_filter = ['housing_type']
    search_fields = ['housing_name']
    prepopulated_fields = {'slug': ('housing_name',)}
    inlines = [HousingImageInline]


admin.site.register(Housing, HousingAdmin)


class RoomImageForm(forms.ModelForm):
    class Meta:
        model = RoomImage
        fields = '__all__'

    images = MultiFileField(min_num=5, max_num=20, max_file_size=1024 * 1024 * 5)


class RoomImageinline(admin.TabularInline):
    model = RoomImage
    form = RoomImageForm
    extra = 1


class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_name', 'housing', 'price_per_night', 'max_guest_capacity', 'room_area')
    list_filter = ('room_name', 'housing', 'max_guest_capacity', 'room_amenities')
    search_fields = ('room_name',)
    inlines = [RoomImageinline]


admin.site.register(Room, RoomAdmin)


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
