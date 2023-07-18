from rest_framework import generics
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from .models import Advertising
from .serializers import AdvertisingSerializer

class AdvertisingAPI(GenericViewSet,
              mixins.ListModelMixin,
              mixins.CreateModelMixin,
              mixins.RetrieveModelMixin,
              mixins.DestroyModelMixin,
              mixins.UpdateModelMixin):
    queryset = Advertising.objects.all()
    serializer_class = AdvertisingSerializer
