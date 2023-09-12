from django_filters import FilterSet, ChoiceFilter, MultipleChoiceFilter, NumberFilter
from .service import get_average_rating
from .constants import *
from .models import Housing


class HousingFilter(FilterSet):
    rating_range = ChoiceFilter(choices=RATING_RANGE_CHOICES, method="filter_by_rating_range",
                                label="Рейтинг по отзывам")

    def filter_by_rating_range(self, queryset, name, value):
        lower_rate, upper_rate = map(int, value.split('-'))
        return queryset.filter(
            id__in=[housing.id for housing in queryset if lower_rate <= get_average_rating(self, housing) <= upper_rate]
        )

    price_per_night__gte = NumberFilter(field_name='rooms__price_per_night', lookup_expr='gte',
                                        label="Минимальная цена за ночь")
    price_per_night__lte = NumberFilter(field_name='rooms__price_per_night', lookup_expr='lte',
                                        label="Максимальная цена за ночь")
    room_amenities = MultipleChoiceFilter(field_name='rooms__room_amenities', choices=ROOM_AMENITIES_CHOICES,
                                          label="Удобства в комнате")
    bed_type = MultipleChoiceFilter(field_name='rooms__bed_type', choices=BED_CHOICES, label="Тип кроватей")

    class Meta:
        model = Housing
        fields = (
            'housing_type', 'accommodation_type', 'food_type', 'stars', 'free_internet',
            'restaurant', 'airport_transfer', 'car_rental', 'gym', 'children_playground', 'park', 'bar',
            'spa_services', 'pool', 'room_service', 'poolside_bar', 'cafe', 'in_room_internet', 'hotel_wide_internet',
            'price_per_night__gte', 'price_per_night__lte', 'rooms__bedrooms', 'room_amenities', 'bed_type',)
