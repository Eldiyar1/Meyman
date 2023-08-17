from rest_framework import viewsets
import requests
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
from googletrans import Translator
from openexchangerates import OpenExchangeRatesClient
from decimal import Decimal


translator = Translator()


class LanguageParamMixin:
    def get_language(self):
        return self.request.query_params.get('lang', 'ru')
    
class CurrencyParaMixin:
    def get_currency(self):
        return self.request.query_params.get('currency', 'USD')

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
        instance = self.get_object()
        lang = self.get_language()

        instance.description = translator.translate(instance.description, dest=lang).text
        instance.housing_type = translator.translate(instance.housing_type, dest=lang).text
        instance.accommodation_type = translator.translate(instance.accommodation_type, dest=lang).text
        instance.bedrooms = translator.translate(instance.bedrooms, dest=lang).text
        instance.bed_type = translator.translate(instance.bed_type, dest=lang).text
        instance.food_type = translator.translate(instance.food_type, dest=lang).text

        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class HousingReservationViewSet(LanguageParamMixin, viewsets.ModelViewSet):
    queryset = HousingReservation.objects.all()
    serializer_class = HousingReservationSerializer
    permission_classes = [IsClientUserOrReadOnly]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        lang = self.get_language()

        instance.destination = translator.translate(instance.destination, dest=lang).text

        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class RoomViewSet(viewsets.ModelViewSet, CurrencyParaMixin):
    queryset = Room.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = RoomFilter
    permission_classes = [IsOwnerUserOrReadOnly]
    pagination_class = StandardResultsSetPagination
    # Define your filter_backends, filterset_class, permission_classes, and pagination_class here
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        base_currency = 'USD'
        target_currency = self.get_currency()
        api_key = '5a3f772434804d4f842dd628f620c198'

        client = OpenExchangeRatesClient(api_key)  

        try:
            exchange_rates = client.latest(base=base_currency)
            if target_currency in exchange_rates['rates']:
                exchange_rate = exchange_rates['rates'][target_currency]

                print("Exchange rate:", exchange_rate)
                print("Original price:", instance.price_per_night)

                # Convert the price
                instance.price_per_night = Decimal(instance.price_per_night) * Decimal(exchange_rate)

                # Debugging output
                print("Converted price:", instance.price_per_night)
        except (OpenExchangeRatesClientException, requests.exceptions.RequestException) as e:
            print("Error while fetching exchange rates:", e)

        serializer = self.get_serializer(instance)
        return Response(serializer.data)

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
