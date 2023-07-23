import django_filters
from .models import Hotel, Hostel, Apartment, GuestHouse, Sanatorium, HousingAmenities, RoomAmenities


class HousingAmenitiesFilter(django_filters.FilterSet):
    class Meta:
        model = HousingAmenities
        fields = {
            'free_internet': ['exact'],
            'spa_services': ['exact'],
            'parking': ['exact'],
            'bar_or_restaurant': ['exact'],
            'pool': ['exact'],
            'airport_transfer': ['exact'],
            'fitness': ['exact'],
            'pet_allowed': ['exact'],
        }


class RoomAmenitiesFilter(django_filters.FilterSet):
    class Meta:
        model = RoomAmenities
        fields = {
            'air_conditioner': ['exact'],
            'hair_dryer': ['exact'],
            'washing_machine': ['exact'],
            'iron': ['exact'],
            'dryer': ['exact'],
            'fridge': ['exact'],
            'tv': ['exact'],
            'microwave': ['exact'],
            'heating': ['exact'],
        }


class AbstractHousingFilter(django_filters.FilterSet):
    amenities = HousingAmenitiesFilter()
    room_amenities = RoomAmenitiesFilter()

    class Meta:
        abstract = True
        fields = {
            'price_per_night': ['gte', 'lte'],
            'beds': ['exact'],
            'food_type': ['exact'],
            'housing_type': ['exact'],
            'accommodation_type': ['exact'],
            'bed_type': ['exact'],
        }


class HotelFilter(AbstractHousingFilter):
    class Meta(AbstractHousingFilter.Meta):
        model = Hotel


class HostelFilter(AbstractHousingFilter):
    class Meta(AbstractHousingFilter.Meta):
        model = Hostel


class ApartmentFilter(AbstractHousingFilter):
    class Meta(AbstractHousingFilter.Meta):
        model = Apartment


class GuestHouseFilter(AbstractHousingFilter):
    class Meta(AbstractHousingFilter.Meta):
        model = GuestHouse


class SanatoriumFilter(AbstractHousingFilter):
    class Meta(AbstractHousingFilter.Meta):
        model = Sanatorium
