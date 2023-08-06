from django_filters import FilterSet, ChoiceFilter, MultipleChoiceFilter, NumberFilter

from .constants import HOUSING_AMENITIES_CHOICES, ROOM_AMENITIES_CHOICES, RATING_CHOICES
from .models import Housing, Room, Hotel, Hostel, Apartment, GuestHouse, Sanatorium


class AbstractHousingFilter(FilterSet):
    housing_amenities = MultipleChoiceFilter(choices=HOUSING_AMENITIES_CHOICES, label="Удобства жилья")
    rating = ChoiceFilter(choices=RATING_CHOICES, label="Рейтинг", method='filter_by_rating')

    def filter_by_rating(self, queryset, name, value):
        return queryset.filter(ratings_received__rating=value)

    class Meta:
        model = Housing
        fields = (
            'housing_type', 'housing_type', 'accommodation_type', 'food_type', 'stars', 'housing_amenities',
        )


class RoomFilter(FilterSet):
    price_per_night__gte = NumberFilter(field_name='price_per_night', lookup_expr='gte')
    price_per_night__lte = NumberFilter(field_name='price_per_night', lookup_expr='lte')
    room_amenities = MultipleChoiceFilter(choices=ROOM_AMENITIES_CHOICES, label="Удобства в комнате")

    class Meta:
        model = Room
        fields = (
            'price_per_night__gte', 'price_per_night__lte', 'bedrooms', 'room_amenities', 'bed_type',
            'without_card', 'free_cancellation', 'payment')


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
