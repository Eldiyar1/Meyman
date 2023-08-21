import requests
from rest_framework import viewsets
from .permissions import IsAdminUserOrReadOnly
from .serializers import CurrencyConverterSerializer
from .utils import create_currency


# Create your models here.
class CurrencyConverterViewSet(viewsets.ViewSet):
    serializer_class = CurrencyConverterSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def create(self, request):
        return create_currency(self, request)
