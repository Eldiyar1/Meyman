from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from googletrans import Translator
from .models import Advertising
from .permissions import IsAdminUserOrReadOnly
from .serializers import AdvertisingSerializer

translator = Translator()


class LanguageParamMixin:
    def get_language(self):
        return self.request.query_params.get('lang', 'ru')


class AdvertisingAPI(ModelViewSet):
    queryset = Advertising.objects.all()
    serializer_class = AdvertisingSerializer
    permission_classes = [IsAdminUserOrReadOnly]


def retrieve(self, request, *args, **kwargs):
    instance = self.get_object()
    lang = self.get_language()

    instance.title = translator.translate(instance.title, dest=lang).text
    instance.text = translator.translate(instance.text, dest=lang).text

    serializer = self.get_serializer(instance)
    return Response(serializer.data)
