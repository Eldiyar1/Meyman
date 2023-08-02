import django_filters

from .constants import HOUSING_AMENITIES_CHOICES, ROOM_AMENITIES_CHOICES
from .models import Hotel, Hostel, Apartment, GuestHouse, Sanatorium, Housing


class AbstractHousingFilter(django_filters.FilterSet):
    price_per_night__gte = django_filters.NumberFilter(field_name='price_per_night', lookup_expr='gte')
    price_per_night__lte = django_filters.NumberFilter(field_name='price_per_night', lookup_expr='lte')
    housing_amenities = django_filters.MultipleChoiceFilter(choices=HOUSING_AMENITIES_CHOICES,
                                                            label="Жилищные удобства")
    room_amenities = django_filters.MultipleChoiceFilter(choices=ROOM_AMENITIES_CHOICES, label="Удобства в комнате")

    class Meta:
        model = Housing
        fields = ('price_per_night__gte', 'price_per_night__lte', 'housing_type', 'accommodation_type', 'bedrooms',
                  'bed_type', 'food_type', 'stars', 'housing_amenities', 'room_amenities',
                  'without_credit_card', 'free_cancellation', 'payment_type')


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
