from rest_framework import viewsets
from .models import Search, Transfer, Car
from .serializers import SearchSerializer, TransferSerializer, CarSerializer
from .filters import SearchFilter, TransferFilter, CarFilter
from django_filters.rest_framework import DjangoFilterBackend


class SearchViewSet(viewsets.ModelViewSet):
    queryset = Search.objects.all()
    serializer_class = SearchSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = SearchFilter


class TransferViewSet(viewsets.ModelViewSet):
    queryset = Transfer.objects.all()
    serializer_class = TransferSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TransferFilter


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CarFilter
