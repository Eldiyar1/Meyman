from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from .paginations import StandardResultsSetPagination, TravelLimitOffsetPagination
from .permissions import IsOwnerUserOrReadOnly, IsClientUserOrReadOnly
from .models import Room, HousingReview, HousingReservation, Sanatorium, House, Apartment, Hostel, Hotel
from .serializers import HousingReviewSerializer, HousingReservationSerializer, RoomGetSerializer, \
    RoomPostSerializer, HousingGetSerializer, HousingPostSerializer, SanatoriumSerializer, HouseSerializer, \
    ApartmentSerializer, HostelSerializer, HotelSerializer
from .filters import RoomFilter, HotelFilter, HostelFilter, ApartmentFilter, HouseFilter, \
    SanatoriumFilter
from .utils import retrieve_currency, LanguageParamMixin, CurrencyParaMixin, retrieve_housetrans, \
    retrieve_reservationtrans


class HousingModelViewSet(LanguageParamMixin, viewsets.ModelViewSet):

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return HousingGetSerializer
        elif self.request.method == 'POST':
            return HousingPostSerializer

    @action(detail=True, methods=['POST'])
    def add_to_favorite(self, request, pk=None):
        instance = self.get_object()
        instance.is_favorite = True
        instance.save()
        return Response('Объект успешно добавлен в избранное!')

    def retrieve(self, request, *args, **kwargs):
        return retrieve_housetrans(self, request, *args, **kwargs)


class HousingReservationViewSet(LanguageParamMixin, viewsets.ModelViewSet):
    queryset = HousingReservation.objects.all()
    serializer_class = HousingReservationSerializer
    permission_classes = [IsClientUserOrReadOnly]

    def retrieve(self, request, *args, **kwargs):
        return retrieve_reservationtrans(self, request, *args, **kwargs)


class RoomViewSet(viewsets.ModelViewSet, CurrencyParaMixin):
    queryset = Room.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = RoomFilter
    permission_classes = [IsOwnerUserOrReadOnly]
    pagination_class = StandardResultsSetPagination

    def retrieve(self, request, *args, **kwargs):
        return retrieve_currency(self, request, *args, **kwargs)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return RoomGetSerializer
        elif self.request.method == 'POST':
            return RoomPostSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = HousingReview.objects.all()
    serializer_class = HousingReviewSerializer
    permission_classes = [IsOwnerUserOrReadOnly]


class HotelViewSet(HousingModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = HotelFilter
    permission_classes = [IsOwnerUserOrReadOnly]
    pagination_class = TravelLimitOffsetPagination


class HostelViewSet(HousingModelViewSet):
    queryset = Hostel.objects.all()
    serializer_class = HostelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = HostelFilter
    permission_classes = [IsOwnerUserOrReadOnly]
    pagination_class = StandardResultsSetPagination


class ApartmentViewSet(HousingModelViewSet):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ApartmentFilter
    permission_classes = [IsOwnerUserOrReadOnly]
    pagination_class = StandardResultsSetPagination


class HouseViewSet(HousingModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = HouseFilter
    permission_classes = [IsOwnerUserOrReadOnly]
    pagination_class = StandardResultsSetPagination


class SanatoriumViewSet(HousingModelViewSet):
    queryset = Sanatorium.objects.all()
    serializer_class = SanatoriumSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = SanatoriumFilter
    permission_classes = [IsOwnerUserOrReadOnly]
    pagination_class = StandardResultsSetPagination
