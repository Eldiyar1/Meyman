from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Transfer, TransferReservation, TransferReview
from .serializers import TransferSerializer, TransferReservationSerializer, TransferReviewSerializer
from .filters import TransferFilter
from .permissions import IsOwnerUserOrReadOnly, IsClientUserOrReadOnly
from .paginations import StandardResultsSetPagination
from .utils import retrieve_translate, retrieve_transfer_translate_review, retrieve_transfer_translate
from ..travel.utils import LanguageParamMixin


class TransferViewSet(viewsets.ModelViewSet, LanguageParamMixin):
    queryset = Transfer.objects.all()
    serializer_class = TransferSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TransferFilter
    # permission_classes = [IsOwnerUserOrReadOnly]
    pagination_class = StandardResultsSetPagination

    def retrieve(self, request, *args, **kwargs):
        return retrieve_transfer_translate(self, request, *args, **kwargs)


class TransferReservationViewSet(LanguageParamMixin, viewsets.ModelViewSet):
    queryset = TransferReservation.objects.all()
    serializer_class = TransferReservationSerializer
    permission_classes = [IsOwnerUserOrReadOnly]

    def retrieve(self, request, *args, **kwargs):
        return retrieve_translate(self, request, *args, **kwargs)


class ReviewViewSet(viewsets.ModelViewSet, LanguageParamMixin):
    queryset = TransferReview.objects.all()
    serializer_class = TransferReviewSerializer
    permission_classes = [IsOwnerUserOrReadOnly]

    def retrieve(self, request, *args, **kwargs):
        return retrieve_transfer_translate_review(self, request, *args, **kwargs)
