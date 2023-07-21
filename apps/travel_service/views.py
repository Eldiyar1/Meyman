from rest_framework import viewsets
from .models import Search, Transfer
from .serializers import SearchSerializer, TransferSerializer

class SearchViewSet(viewsets.ModelViewSet):
    queryset = Search.objects.all()
    serializer_class = SearchSerializer

class TransferViewSet(viewsets.ModelViewSet):
    queryset = Transfer.objects.all()
    serializer_class = TransferSerializer

