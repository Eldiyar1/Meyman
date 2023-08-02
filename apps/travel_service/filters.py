import django_filters
from .models import *


class SearchFilter(django_filters.FilterSet):
    class Meta:
        model = Search
        fields = '__all__'


class TransferFilter(django_filters.FilterSet):
    class Meta:
        model = Transfer
        fields = '__all__'


class CarFilter(django_filters.FilterSet):
    min_rental_price = django_filters.NumberFilter(field_name='rental_price', lookup_expr='gte')
    max_rental_price = django_filters.NumberFilter(field_name='rental_price', lookup_expr='lte')

    class Meta:
        model = Car
        fields = ('min_rental_price', 'max_rental_price', 'brand', 'color', 'body_type', 'steering', 'drive_type',
                  'passenger_capacity', 'fuel_type', 'condition', 'transmission')
