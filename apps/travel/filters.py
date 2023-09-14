from django_filters import FilterSet, ChoiceFilter, MultipleChoiceFilter, NumberFilter
from .service import get_average_rating
from .constants import *
from .models import Housing
from ..travel_service.constants import DESTINATION_CHOICES


class HousingFilter(FilterSet):
    rating_range = ChoiceFilter(choices=RATING_RANGE_CHOICES, method="filter_by_rating_range",
                                label="Рейтинг по отзывам")
    region = ChoiceFilter(field_name='region', choices=DESTINATION_CHOICES, label="Область")

    check_in_time_start = ChoiceFilter(choices=TIME_CHOICES, label='Время заезда')
    check_out_time_start = ChoiceFilter(choices=TIME_CHOICES, label='Время выезда')

    def filter_by_rating_range(self, queryset, name, value):
        lower_rate, upper_rate = map(int, value.split('-'))
        return queryset.filter(
            id__in=[housing.id for housing in queryset if lower_rate <= get_average_rating(self, housing) <= upper_rate]
        )

    max_guest_capacity = NumberFilter(field_name='rooms__max_guest_capacity', lookup_expr='gte',
                                      label="максимальное количестко гостей")


    price_per_night__gte = NumberFilter(field_name='rooms__price_per_night', lookup_expr='gte',
                                        label="Минимальная цена за ночь")
    price_per_night__lte = NumberFilter(field_name='rooms__price_per_night', lookup_expr='lte',
                                        label="Максимальная цена за ночь")
    room_amenities = MultipleChoiceFilter(field_name='rooms__room_amenities', lookup_expr="icontains",
                                          choices=ROOM_AMENITIES_CHOICES, label="Удобства в комнате")
    bed_type = MultipleChoiceFilter(field_name='rooms__bed_type', lookup_expr="icontains",
                                    choices=BED_CHOICES, label="Тип кроватей")

    class Meta:
        model = Housing
        fields = (
            'housing_type', 'accommodation_type', 'food_type', 'stars', 'free_internet',
            'restaurant', 'airport_transfer', 'car_rental', 'gym', 'children_playground', 'park', 'bar',
            'spa_services', 'pool', 'room_service', 'poolside_bar', 'cafe', 'in_room_internet', 'hotel_wide_internet',
            'price_per_night__gte', 'price_per_night__lte', 'rooms__bedrooms', 'room_amenities', 'bed_type',
            "region", "check_out_time_start", "check_in_time_start", "max_guest_capacity"
        )
