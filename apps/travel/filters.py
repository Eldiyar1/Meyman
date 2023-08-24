from django_filters import FilterSet, ChoiceFilter, MultipleChoiceFilter, NumberFilter
from .service import get_average_rating
from .constants import HOUSING_AMENITIES_CHOICES, ROOM_AMENITIES_CHOICES, RATING_RANGE_CHOICES
from .models import Housing, Room


class HousingFilter(FilterSet):
    housing_amenities = MultipleChoiceFilter(choices=HOUSING_AMENITIES_CHOICES, label="Удобства жилья")
    rating_range = ChoiceFilter(choices=RATING_RANGE_CHOICES, method="filter_by_rating_range",
                                label="Рейтинг по отзывам")

    def filter_by_rating_range(self, queryset, name, value):
        lower_rate, upper_rate = map(int, value.split('-'))
        return queryset.filter(
            id__in=[housing.id for housing in queryset if lower_rate <= get_average_rating(self, housing) <= upper_rate]
        )

    class Meta:
        model = Housing
        fields = ('housing_type', 'accommodation_type', 'food_type', 'stars', 'free_internet',
                  'restaurant', 'restaurant', 'airport_transfer', 'park', 'spa_services', 'bar', 'pool', 'room_service',
                  'poolside_bar', 'cafe', 'in_room_internet', 'hotel_wide_internet')


class RoomFilter(FilterSet):
    price_per_night__gte = NumberFilter(field_name='price_per_night', lookup_expr='gte')
    price_per_night__lte = NumberFilter(field_name='price_per_night', lookup_expr='lte')
    room_amenities = MultipleChoiceFilter(choices=ROOM_AMENITIES_CHOICES, label="Удобства в комнате")

    class Meta:
        model = Room
        fields = ('price_per_night__gte', 'price_per_night__lte', 'bedrooms', 'room_amenities', 'bed_type',)