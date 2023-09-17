from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response

from .paginations import StandardResultsSetPagination, TravelLimitOffsetPagination
from .permissions import IsOwnerUserOrReadOnly, IsClientUserOrReadOnly, IsrMineOrReadOnly, IsOwnerUserOrReadOnlyForRooms
from .models import HousingReview, HousingReservation, Housing, Room, HousingAvailability, \
    HousingImage, RoomImage
from .serializers import HousingReviewSerializer, HousingReservationSerializer, RoomGetSerializer, RoomPostSerializer, \
    HousingGetSerializer, HousingPostSerializer, \
    HousingAvailabilityPostSerializer, HousingImageSerializer, HousingAvailabilityGetSerializer, \
    ConvertedRoomSerializer, RoomImageSerializer
from .filters import HousingFilter
from .utils import perform_create, annotate_housing_queryset, retrieve_housetrans, \
    retrieve_room, LanguageParamMixin


class HousingViewSet(viewsets.ModelViewSet, LanguageParamMixin):
    queryset = Housing.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = HousingFilter
    permission_classes = [IsOwnerUserOrReadOnly]
    pagination_class = TravelLimitOffsetPagination
    ordering_fields = ['stars', 'rooms__price_per_night', 'average_rating', 'review_count']
    serializer_class = HousingPostSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return HousingGetSerializer
        return self.serializer_class

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        currency = self.request.query_params.get('currency', 'USD')
        rooms = instance.rooms.all()
        converted_rooms = ConvertedRoomSerializer(rooms, many=True, context={'currency': currency}).data
        data = HousingGetSerializer(instance).data
        data['rooms'] = converted_rooms
        return Response(data)

    def get_queryset(self):
        queryset = super().get_queryset()
        annotated_queryset = annotate_housing_queryset(queryset)
        return annotated_queryset

    def housetrans(self, serializer, *args, **kwargs):
        return retrieve_housetrans(self, serializer)


class HousingReservationViewSet(viewsets.ModelViewSet):
    queryset = HousingReservation.objects.all()
    serializer_class = HousingReservationSerializer
    permission_classes = [IsrMineOrReadOnly]

    def perform_create(self, serializer, *args, **kwargs):
        serializer.save(user=self.request.user)
        return perform_create(self, serializer)

    def get_queryset(self):
        return HousingReservation.objects.filter(user=self.request.user)


class HousingAvailabilityViewSet(viewsets.ModelViewSet):
    queryset = HousingAvailability.objects.all()
    serializer_class = HousingAvailabilityPostSerializer
    permission_classes = [IsOwnerUserOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return HousingAvailabilityGetSerializer
        return self.serializer_class


class RoomViewSet(viewsets.ModelViewSet, LanguageParamMixin):
    queryset = Room.objects.all()
    permission_classes = [IsOwnerUserOrReadOnlyForRooms]
    pagination_class = StandardResultsSetPagination
    serializer_class = RoomPostSerializer

    

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return RoomGetSerializer
        return self.serializer_class


    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['currency'] = self.request.query_params.get('currency', 'USD')
        return context

    def room_translate(self, serializer, *args, **kwargs):
        return retrieve_room(self, serializer)


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = HousingReview.objects.all()
    serializer_class = HousingReviewSerializer
    permission_classes = [IsClientUserOrReadOnly]


class HousingImageViewSet(viewsets.ModelViewSet):
    queryset = HousingImage.objects.all()
    serializer_class = HousingImageSerializer
    permission_classes = [IsOwnerUserOrReadOnly]


class RoomsImagesViewSet(viewsets.ModelViewSet):
    queryset = RoomImage.objects.all()
    serializer_class = RoomImageSerializer
    permission_classes = [IsOwnerUserOrReadOnlyForRooms]
