from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from .paginations import StandardResultsSetPagination, TravelLimitOffsetPagination
from .permissions import IsOwnerUserOrReadOnly, IsClientUserOrReadOnly
from .models import HousingReview, HousingReservation, Housing, Room
from .serializers import HousingReviewSerializer, HousingReservationSerializer, RoomGetSerializer, \
    RoomPostSerializer, HousingGetSerializer, HousingPostSerializer
from .filters import RoomFilter, HousingFilter
from .utils import retrieve_currency, LanguageParamMixin, CurrencyParaMixin, retrieve_housetrans, \
    retrieve_reservationtrans


class HousingViewSet(LanguageParamMixin, viewsets.ModelViewSet):
    queryset = Housing.objects.all()
    serializer_class = HousingPostSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = HousingFilter
    permission_classes = [IsOwnerUserOrReadOnly]
    pagination_class = TravelLimitOffsetPagination

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
