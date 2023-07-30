from rest_framework import viewsets
from .models import Search, Transfer
from .serializers import SearchSerializer, TransferSerializer
from .filters import SearshFilter, TransferFilter
from django_filters.rest_framework import DjangoFilterBackend


class SearchViewSet(viewsets.ModelViewSet):
    queryset = Search.objects.all()
    serializer_class = SearchSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = SearshFilter


class TransferViewSet(viewsets.ModelViewSet):
    queryset = Transfer.objects.all()
    serializer_class = TransferSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TransferFilter
