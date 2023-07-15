from rest_framework.viewsets import ModelViewSet
from travel.models import TravelService, Hotel, News
from travel.serializers import TravelServiceSerializer, HotelSerializer, NewsSerializer
from .permissions import IsAdminUserOrReadOnly


class TravelServiceViewSet(ModelViewSet):
    queryset = TravelService.objects.all()
    serializer_class = TravelServiceSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class HotelViewSet(ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class NewsViewSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsAdminUserOrReadOnly]
