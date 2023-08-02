from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from .models import Hotel, Hostel, Apartment, GuestHouse, Sanatorium
from .serializers import HotelSerializer, HostelSerializer, ApartmentSerializer, GuestHouseSerializer, \
    SanatoriumSerializer
from .filters import HotelFilter, HostelFilter, ApartmentFilter, GuestHouseFilter, SanatoriumFilter
from googletrans import Translator

translator = Translator()


class LanguageParamMixin:
    def get_language(self):
        return self.request.query_params.get('lang', 'ru')


class AbstractHousingModelViewSet(LanguageParamMixin, mixins.ListModelMixin,
                                  mixins.CreateModelMixin,
                                  mixins.RetrieveModelMixin,
                                  mixins.UpdateModelMixin,
                                  mixins.DestroyModelMixin,
                                  viewsets.GenericViewSet):
    pass


class HotelViewSet(AbstractHousingModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = HotelFilter

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


class HostelViewSet(AbstractHousingModelViewSet):
    queryset = Hostel.objects.all()
    serializer_class = HostelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = HostelFilter

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


class ApartmentViewSet(AbstractHousingModelViewSet):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ApartmentFilter

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


class GuestHouseViewSet(AbstractHousingModelViewSet):
    queryset = GuestHouse.objects.all()
    serializer_class = GuestHouseSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = GuestHouseFilter

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


class SanatoriumViewSet(AbstractHousingModelViewSet):
    queryset = Sanatorium.objects.all()
    serializer_class = SanatoriumSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = SanatoriumFilter

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
