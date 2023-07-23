import django_filters
from .models import AccommodationReservation

class AccommodationReservationFilter(django_filters.FilterSet):
    booking_type = django_filters.ChoiceFilter(choices=AccommodationReservation.BOOKING_CHOICES)
    payment_type = django_filters.ChoiceFilter(choices=AccommodationReservation.PAYMENT_CHOICES)

    class Meta:
        model = AccommodationReservation
        fields = {
            'booking_type': ['exact'],
            'payment_type': ['exact'],
        }