import django_filters
from .models import Hotel, Hostel, Apartment, GuestHouse, Sanatorium, HousingAmenities, RoomAmenities


class HousingAmenitiesFilter(django_filters.FilterSet):
    class Meta:
        model = HousingAmenities
        fields = ('free_internet', 'spa_services', 'bar_or_restaurant', 'pool', 'airport_transfer',
                  'fitness', 'pet_allowed')

class RoomAmenitiesFilter(django_filters.FilterSet):
    class Meta:
        model = RoomAmenities
        fields = ('air_conditioner', 'hair_dryer', 'washing_machine', 'iron', 'dryer', 'fridge', 'tv', 'microwave',
                  'heating')


class AbstractHousingFilter(django_filters.FilterSet):
    amenities = HousingAmenitiesFilter()
    room_amenities = RoomAmenitiesFilter()

    price_per_night__gte = django_filters.NumberFilter(field_name='price_per_night', lookup_expr='gte')
    price_per_night__lte = django_filters.NumberFilter(field_name='price_per_night', lookup_expr='lte')

    class Meta:
        abstract = True
        fields = ('price_per_night__gte', 'price_per_night__lte', 'beds', 'food_type', 'housing_type',
            'accommodation_type', 'bedrooms', 'bed_type', 'parking_service')


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
