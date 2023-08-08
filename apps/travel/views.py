from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import IsRegisteredUserOrReadOnly
from .models import Hotel, Hostel, Apartment, GuestHouse, Sanatorium, Rating, HouseReservation, Room, HouseFavorite, \
    Housing

from .serializers import HotelSerializer, HostelSerializer, ApartmentSerializer, GuestHouseSerializer, \
    SanatoriumSerializer, RatingSerializer, HouseReservationSerializer, RoomSerializer, HouseFavoriteSerializer
from .filters import HotelFilter, HostelFilter, ApartmentFilter, GuestHouseFilter, SanatoriumFilter, RoomFilter
from googletrans import Translator

translator = Translator()


class LanguageParamMixin:
    def get_language(self):
        return self.request.query_params.get('lang', 'ru')


class AbstractHousingModelViewSet(LanguageParamMixin, viewsets.ModelViewSet):

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


class HouseFavoriteViewSet(mixins.ListModelMixin,
                           mixins.CreateModelMixin,
                           mixins.DestroyModelMixin,
                           viewsets.GenericViewSet):
    queryset = HouseFavorite.objects.all()
    serializer_class = HouseFavoriteSerializer
    permission_classes = [IsRegisteredUserOrReadOnly]

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
class HouseReservationViewSet(LanguageParamMixin, viewsets.ModelViewSet):
    queryset = HouseReservation.objects.all()
    serializer_class = HouseReservationSerializer
    permission_classes = [IsRegisteredUserOrReadOnly]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        lang = self.get_language()

        instance.destination = translator.translate(instance.destination, dest=lang).text

        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class HotelViewSet(AbstractHousingModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = HotelFilter
    permission_classes = [IsRegisteredUserOrReadOnly]


class HostelViewSet(AbstractHousingModelViewSet):
    queryset = Hostel.objects.all()
    serializer_class = HostelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = HostelFilter
    permission_classes = [IsRegisteredUserOrReadOnly]


class ApartmentViewSet(AbstractHousingModelViewSet):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ApartmentFilter
    permission_classes = [IsRegisteredUserOrReadOnly]


class GuestHouseViewSet(AbstractHousingModelViewSet):
    queryset = GuestHouse.objects.all()
    serializer_class = GuestHouseSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = GuestHouseFilter
    permission_classes = [IsRegisteredUserOrReadOnly]


class SanatoriumViewSet(AbstractHousingModelViewSet):
    queryset = Sanatorium.objects.all()
    serializer_class = SanatoriumSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = SanatoriumFilter
    permission_classes = [IsRegisteredUserOrReadOnly]


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = RoomFilter
    permission_classes = [IsRegisteredUserOrReadOnly]


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsRegisteredUserOrReadOnly]
