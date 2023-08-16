from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import IsOwnerUserOrReadOnly, IsClientUserOrReadOnly
from .models import Room, HousingReview, HousingReservation, Housing
from .serializers import HousingReviewSerializer, HousingReservationSerializer, RoomGetSerializer, \
    RoomPostSerializer, HousingGetSerializer, HousingPostSerializer
from .filters import RoomFilter, HousingFilter
from googletrans import Translator

translator = Translator()


class LanguageParamMixin:
    def get_language(self):
        return self.request.query_params.get('lang', 'ru')


class HousingModelViewSet(LanguageParamMixin, viewsets.ModelViewSet):
    queryset = Housing.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = HousingFilter
    permission_classes = [IsOwnerUserOrReadOnly]

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


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = RoomFilter
    permission_classes = [IsOwnerUserOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return RoomGetSerializer
        elif self.request.method == 'POST':
            return RoomPostSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = HousingReview.objects.all()
    serializer_class = HousingReviewSerializer
    permission_classes = [IsOwnerUserOrReadOnly]