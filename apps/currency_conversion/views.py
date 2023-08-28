from rest_framework import viewsets
from .serializers import CurrencyConversionSerializer
from .permissions import IsAdminUserOrReadOnly
from .utils import CurrencyiewSet



class CurrencyConverterViewSet(viewsets.ModelViewSet):
    serializer_class = CurrencyConversionSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    currency_view_set = CurrencyiewSet()  

    def create(self, request):
        return self.currency_view_set.create(request)  

