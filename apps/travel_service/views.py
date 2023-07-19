from rest_framework import mixins, viewsets
from .models import TravelService
from .permissions import IsAdminUserOrReadOnly
from .serializers import TravelServiceSerializer


class TravelServiceViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    queryset = TravelService.objects.all()
    serializer_class = TravelServiceSerializer
    permission_classes = [IsAdminUserOrReadOnly]