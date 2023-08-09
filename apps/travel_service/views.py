from rest_framework import viewsets
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from googletrans import Translator
from .models import Transfer, TransferReservation
from .serializers import TransferSerializer, TransferReservationSerializer
from .filters import TransferFilter
from .permissions import IsOwnerUserOrReadOnly, IsClientUserOrReadOnly
translator = Translator()


class LanguageParamMixin:
    def get_language(self):
        return self.request.query_params.get('lang', 'ru')


class TransferViewSet(viewsets.ModelViewSet):
    queryset = Transfer.objects.all()
    serializer_class = TransferSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TransferFilter
    permission_classes = [IsOwnerUserOrReadOnly]


class TransferReservationViewSet(LanguageParamMixin, viewsets.ModelViewSet):
    queryset = TransferReservation.objects.all()
    serializer_class = TransferReservationSerializer
    permission_classes = [IsClientUserOrReadOnly]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        lang = self.get_language()

        instance.transfer_location = translator.translate(instance.transfer_location, dest=lang).text
        instance.return_location = translator.translate(instance.return_location, dest=lang).text

        serializer = self.get_serializer(instance)
        return Response(serializer.data)
