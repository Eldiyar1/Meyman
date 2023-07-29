
import django_filters
from .models import AccommodationReservation

class AccommodationReservationFilter(django_filters.FilterSet):
    class Meta:
        model = AccommodationReservation
        fields = {
            'booking_type': ['exact'],
            'payment_type': ['exact'],
        }

