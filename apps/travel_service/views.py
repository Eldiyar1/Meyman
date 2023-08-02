from rest_framework import viewsets
from rest_framework.response import Response

from .models import Search, Transfer, Car
from .serializers import SearchSerializer, TransferSerializer, CarSerializer
from .filters import SearchFilter, TransferFilter, CarFilter
from django_filters.rest_framework import DjangoFilterBackend
from googletrans import Translator

translator = Translator()

class LanguageParamMixin:
    def get_language(self):
        return self.request.query_params.get('lang', 'ru')


class SearchViewSet(LanguageParamMixin, viewsets.ModelViewSet):
    queryset = Search.objects.all()
    serializer_class = SearchSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = SearchFilter

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        lang = self.get_language()

        instance.destination = translator.translate(instance.destination, dest=lang).text

        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class TransferViewSet(LanguageParamMixin, viewsets.ModelViewSet):
    queryset = Transfer.objects.all()
    serializer_class = TransferSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_class = TransferFilter

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        lang = self.get_language()


        instance.transfer_location = translator.translate(instance.transfer_location, dest=lang).text
        instance.return_location = translator.translate(instance.return_location, dest=lang).text

        serializer = self.get_serializer(instance)

        return Response(serializer.data)


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CarFilter
