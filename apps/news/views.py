from rest_framework import viewsets
from rest_framework.response import Response
from .models import News
from .permissions import IsAdminUserOrReadOnly
from .serializers import NewsSerializer
from googletrans import Translator

translator = Translator()

class LanguageParamMixin:
    def get_language(self):
        return self.request.query_params.get('lang', 'ru')



class NewsViewSet(LanguageParamMixin, viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        lang = self.get_language()

        # Translate the fields
        instance.title = translator.translate(instance.title, dest=lang).text
        instance.content = translator.translate(instance.content, dest=lang).text

        serializer = self.get_serializer(instance)
        return Response(serializer.data)
