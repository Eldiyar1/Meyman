from rest_framework import generics
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from .models import Advertising
from .serializers import AdvertisingSerializer
from rest_framework.response import Response
from googletrans import Translator

translator = Translator()


class LanguageParamMixin:
    def get_language(self):
        return self.request.query_params.get('lang', 'ru')  

class AdvertisingAPI(LanguageParamMixin, GenericViewSet,
              mixins.ListModelMixin,
              mixins.CreateModelMixin,
              mixins.RetrieveModelMixin,
              mixins.DestroyModelMixin,
              mixins.UpdateModelMixin):
    queryset = Advertising.objects.all()
    serializer_class = AdvertisingSerializer


    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        lang = self.get_language()

        instance.title = translator.translate(instance.title, dest=lang).text
        instance.text = translator.translate(instance.text, dest=lang).text

        serializer = self.get_serializer(instance)
        return Response(serializer.data)