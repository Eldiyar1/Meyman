from rest_framework import mixins, viewsets
from .models import PriceRange, HousingType, AccommodationType, BedType, Hotel, Hostel, Apartment, GuestHouse, \
    TravelService, Author, News
from .permissions import IsAdminUserOrReadOnly
from .serializers import PriceRangeSerializer, HousingTypeSerializer, AccommodationTypeSerializer, BedTypeSerializer, \
    HotelSerializer, HostelSerializer, ApartmentSerializer, GuestHouseSerializer, TravelServiceSerializer, \
    AuthorSerializer, NewsSerializer


class AbstractModelViewSet(mixins.ListModelMixin,
                           mixins.CreateModelMixin,
                           mixins.RetrieveModelMixin,
                           mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin,
                           viewsets.GenericViewSet):
    pass


class PriceRangeViewSet(AbstractModelViewSet):
    queryset = PriceRange.objects.all()
    serializer_class = PriceRangeSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class HousingTypeViewSet(AbstractModelViewSet):
    queryset = HousingType.objects.all()
    serializer_class = HousingTypeSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class AccommodationTypeViewSet(AbstractModelViewSet):
    queryset = AccommodationType.objects.all()
    serializer_class = AccommodationTypeSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class BedTypeViewSet(AbstractModelViewSet):
    queryset = BedType.objects.all()
    serializer_class = BedTypeSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class HotelViewSet(AbstractModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class HostelViewSet(AbstractModelViewSet):
    queryset = Hostel.objects.all()
    serializer_class = HostelSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class ApartmentViewSet(AbstractModelViewSet):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class GuestHouseViewSet(AbstractModelViewSet):
    queryset = GuestHouse.objects.all()
    serializer_class = GuestHouseSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class TravelServiceViewSet(AbstractModelViewSet):
    queryset = TravelService.objects.all()
    serializer_class = TravelServiceSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class AuthorViewSet(AbstractModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class NewsViewSet(AbstractModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsAdminUserOrReadOnly]
