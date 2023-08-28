from rest_framework import viewsets
from .serializers import CurrencyConversionSerializer
from .permissions import IsAdminUserOrReadOnly
from .utils import CurrencyiewSet
from rest_framework.response import Response



class CurrencyConverterViewSet(viewsets.ViewSet):
    serializer_class = CurrencyConversionSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    currency_view_set = CurrencyiewSet()  # Создание экземпляра CurrencyiewSet

    def get_queryset(self):
        return None  # Возвращаем пустой QuerySet, чтобы избежать ошибки

    def list(self, request):
        return Response([])  # Возвращаем пустой список для метода list

    def create(self, request):
        return self.currency_view_set.create(request) 
