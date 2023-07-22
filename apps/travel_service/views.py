from rest_framework import viewsets
from rest_framework.response import Response
from .models import Search, Transfer
from .serializers import SearchSerializer, TransferSerializer
from googletrans import Translator

translator = Translator()

class LanguageParamMixin:
    def get_language(self):
        return self.request.query_params.get('lang', 'ru')



class SearchViewSet(viewsets.ModelViewSet):
    queryset = Search.objects.all()
    serializer_class = SearchSerializer

class TransferViewSet(LanguageParamMixin, viewsets.ModelViewSet):
    queryset = Transfer.objects.all()
    serializer_class = TransferSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        lang = self.get_language()

        # Translate the fields
        instance.transfer_location = translator.translate(instance.transfer_location, dest=lang).text
        instance.return_location = translator.translate(instance.return_location, dest=lang).text

        serializer = self.get_serializer(instance)
        return Response(serializer.data)