from rest_framework import mixins, viewsets
from .models import Hotel, Hostel, Apartment, GuestHouse, Sanatorium
from .permissions import IsAdminUserOrReadOnly
from .serializers import HotelSerializer, HostelSerializer, ApartmentSerializer, GuestHouseSerializer, \
    SanatoriumSerializer


class AbstractHousingModelViewSet(mixins.ListModelMixin,
                                  mixins.CreateModelMixin,
                                  mixins.RetrieveModelMixin,
                                  mixins.UpdateModelMixin,
                                  mixins.DestroyModelMixin,
                                  viewsets.GenericViewSet):
    pass


class HotelViewSet(AbstractHousingModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class HostelViewSet(AbstractHousingModelViewSet):
    queryset = Hostel.objects.all()
    serializer_class = HostelSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class ApartmentViewSet(AbstractHousingModelViewSet):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class GuestHouseViewSet(AbstractHousingModelViewSet):
    queryset = GuestHouse.objects.all()
    serializer_class = GuestHouseSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class SanatoriumViewSet(AbstractHousingModelViewSet):
    queryset = Sanatorium.objects.all()
    serializer_class = SanatoriumSerializer
    permission_classes = [IsAdminUserOrReadOnly]
