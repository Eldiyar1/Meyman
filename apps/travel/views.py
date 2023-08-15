from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from googletrans import Translator
from .permissions import IsOwnerUserOrReadOnly, IsClientUserOrReadOnly
from .paginations import StandardResultsSetPagination
from .models import Room, HousingReview, HousingReservation, Hotel, Hostel, Apartment, House, Sanatorium
from .serializers import RoomSerializer, HousingReviewSerializer, HousingReservationSerializer, \
    HotelSerializer, HostelSerializer, ApartmentSerializer, HouseSerializer, SanatoriumSerializer
from .filters import RoomFilter, HotelFilter, HostelFilter, ApartmentFilter, HouseFilter, \
    SanatoriumFilter

translator = Translator()


class LanguageParamMixin:
    def get_language(self):
        return self.request.query_params.get('lang', 'ru')


class HousingModelViewSet(LanguageParamMixin, viewsets.ModelViewSet):


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


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = RoomFilter
    permission_classes = [IsOwnerUserOrReadOnly]
    pagination_class = StandardResultsSetPagination



class ReviewViewSet(viewsets.ModelViewSet):
    queryset = HousingReview.objects.all()
    serializer_class = HousingReviewSerializer
    permission_classes = [IsClientUserOrReadOnly]


class HotelViewSet(HousingModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = HotelFilter
    permission_classes = [IsOwnerUserOrReadOnly]
    pagination_class = StandardResultsSetPagination



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


