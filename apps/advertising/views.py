from rest_framework.viewsets import ModelViewSet
from googletrans import Translator
from .models import Advertising
from .permissions import IsAdminUserOrReadOnly
from .serializers import AdvertisingSerializer
from .utils import retrieve_trans



class AdvertisingAPI(ModelViewSet):
    queryset = Advertising.objects.all()
    serializer_class = AdvertisingSerializer
    permission_classes = [IsAdminUserOrReadOnly]


def retrieve(self, request, *args, **kwargs):
   return retrieve_trans(self, request, *args, **kwargs)
