import django_filters
from .models import AccommodationReservation
from .constants import BOOKING_CHOICES, PAYMENT_CHOICES

class AccommodationReservationFilter(django_filters.FilterSet):
    booking_type = django_filters.ChoiceFilter(choices=BOOKING_CHOICES)
    payment_type = django_filters.ChoiceFilter(choices=PAYMENT_CHOICES)

    class Meta:
        model = AccommodationReservation
        fields = {
            'booking_type': ['exact'],
            'payment_type': ['exact'],
        }
