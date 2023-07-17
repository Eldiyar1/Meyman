from rest_framework import mixins, viewsets
from .models import *
from .serializers import TravelServiceSerializer, HotelSerializer, NewsSerializer, SignalSerializer
from .permissions import IsAdminUserOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from .paginations import *
from django.contrib.auth.models import User
from .models import create_signal


class TravelServiceViewSet(mixins.ListModelMixin,
                           mixins.CreateModelMixin,
                           mixins.RetrieveModelMixin,
                           mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin,
                           viewsets.GenericViewSet):
    queryset = TravelService.objects.all()
    serializer_class = TravelServiceSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = 'service_name description price location is_available'.split()
    pagination_class = StandardResultsSetPagination
    search_fields = ['service_name', 'description', 'price', 'location', 'is_available']


class HotelViewSet(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = 'hotel_name description daily_price available_rooms is_available'.split()
    pagination_class = StandardResultsSetPagination
    search_fields = ['hotel_name', 'description', 'daily_price', 'is_available', 'available_rooms']


class NewsViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = 'title author published_date content'.split()
    pagination_class = StandardResultsSetPagination
    search_fields = ['title', 'author', 'published_date', 'content']


class SignalViewSet(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    queryset = Signal.objects.all()
    serializer_class = SignalSerializer
    def get(self, request, *args, **kwargs):
        user = User.objects.get(username='john')
        message = 'Новое уведомление!'
        create_signal(user, message)

    def post(self, request, *args, **kwargs):
        user = User.objects.get(username='john')
        message = 'Новое уведомление!'
        create_signal(user, message)
