from rest_framework import mixins, viewsets
from .models import TravelService, Hotel, News
from .serializers import TravelServiceSerializer, HotelSerializer, NewsSerializer
from .permissions import IsAdminUserOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from .paginations import *

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
    filterset_fields = 'service_name price location is_available'.split()
    pagination_class = StandardResultsSetPagination
    search_fields = ['service_name', 'price', 'location', 'is_available']



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


