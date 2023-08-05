from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

from .models import Hotel, Hostel, Apartment, GuestHouse, Sanatorium, Rating, HouseReservation, HouseFavorite,Housing
from .serializers import HotelSerializer, HostelSerializer, ApartmentSerializer, GuestHouseSerializer, \
    SanatoriumSerializer, RatingSerializer, HouseReservationSerializer, HouseFavoriteSerializer
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


class HouseReservationViewSet(LanguageParamMixin, viewsets.ModelViewSet):
    queryset = HouseReservation.objects.all()
    serializer_class = HouseReservationSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        lang = self.get_language()

        instance.destination = translator.translate(instance.destination, dest=lang).text

        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class HouseFavoriteViewSet(mixins.ListModelMixin,
                           mixins.CreateModelMixin,
                           mixins.DestroyModelMixin,
                           viewsets.GenericViewSet):
    queryset = HouseFavorite.objects.all()
    serializer_class = HouseFavoriteSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['POST'])
    def add(self, request):
        post_id = request.data.get('post_id')
        try:
            post = Housing.objects.get(id=post_id)
            favorite, created = HouseFavorite.objects.get_or_create(user=request.user, item=post)
            if created:
                return Response({'message': 'Добавлено в избранное.'}, status=status.HTTP_201_CREATED)
            else:
                return Response({'message': 'Уже в избранном.'}, status=status.HTTP_200_OK)
        except Housing.DoesNotExist:
            return Response({'message': 'Пост не найден.'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['POST'])
    def remove(self, request):
        post_id = request.data.get('post_id')
        try:
            favorite = HouseFavorite.objects.get(user=request.user, item_id=post_id)
            favorite.delete()
            return Response({'message': 'Удалено из избранного.'}, status=status.HTTP_200_OK)
        except HouseFavorite.DoesNotExist:
            return Response({'message': 'Не найдено в избранном.'}, status=status.HTTP_404_NOT_FOUND)


class HotelViewSet(AbstractHousingModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = HotelFilter


class HostelViewSet(AbstractHousingModelViewSet):
    queryset = Hostel.objects.all()
    serializer_class = HostelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = HostelFilter


class ApartmentViewSet(AbstractHousingModelViewSet):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ApartmentFilter


class GuestHouseViewSet(AbstractHousingModelViewSet):
    queryset = GuestHouse.objects.all()
    serializer_class = GuestHouseSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = GuestHouseFilter


class SanatoriumViewSet(AbstractHousingModelViewSet):
    queryset = Sanatorium.objects.all()
    serializer_class = SanatoriumSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = SanatoriumFilter


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
