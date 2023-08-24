from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from .paginations import StandardResultsSetPagination, TravelLimitOffsetPagination
from .permissions import IsOwnerUserOrReadOnly, IsClientUserOrReadOnly
from .models import HousingReview, HousingReservation, Housing, Room, HousingAvailability
from .serializers import HousingReviewSerializer, HousingReservationSerializer, HousingAvailabilitySerializer
from .filters import HousingFilter, RoomFilter
from .utils import retrieve_currency, CurrencyParaMixin, get_housing_serializer_class, get_room_serializer_class


class HousingViewSet(viewsets.ModelViewSet):
    queryset = Housing.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = HousingFilter
    permission_classes = [IsOwnerUserOrReadOnly]
    pagination_class = TravelLimitOffsetPagination
    ordering_fields = ['stars', ]

    def get_serializer_class(self):
        return get_housing_serializer_class(self.request.method)

    @action(detail=True, methods=['POST'])
    def add_to_favorite(self, request, pk=None):
        instance = self.get_object()
        instance.is_favorite = True
        instance.save()
        return Response('Объект успешно добавлен в избранное!')

    # def retrieve(self, request, *args, **kwargs):
    #     return retrieve_housetrans(self, request, *args, **kwargs)


class HousingReservationViewSet(viewsets.ModelViewSet):
    queryset = HousingReservation.objects.all()
    serializer_class = HousingReservationSerializer
    permission_classes = [IsClientUserOrReadOnly]

    # def retrieve(self, request, *args, **kwargs):
    #     return retrieve_reservationtrans(self, request, *args, **kwargs)


class HousingAvailabilityViewSet(viewsets.ModelViewSet):
    queryset = HousingAvailability.objects.all()
    serializer_class = HousingAvailabilitySerializer
    permission_classes = [IsOwnerUserOrReadOnly]

    def availability(self, request, pk=None):
        housing = self.get_object()
        availability = HousingAvailability.objects.filter(housing=housing)
        serializer = HousingAvailabilitySerializer(availability, many=True)
        return Response(serializer.data)


class RoomViewSet(viewsets.ModelViewSet, CurrencyParaMixin):
    queryset = Room.objects.all()
    permission_classes = [IsOwnerUserOrReadOnly]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = RoomFilter
    ordering_fields = ['price_per_night']
    pagination_class = StandardResultsSetPagination

    def get_serializer_class(self):
        return get_room_serializer_class(self.request.method)

    def retrieve(self, request, *args, **kwargs):
        return retrieve_currency(self, request, *args, **kwargs)


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = HousingReview.objects.all()
    serializer_class = HousingReviewSerializer
    permission_classes = [IsOwnerUserOrReadOnly]
