from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import News
from .permissions import IsRegisteredUserOrReadOnly
from .serializers import NewsSerializer
from .filters import NewsFilter
from googletrans import Translator

translator = Translator()


class LanguageParamMixin:
    def get_language(self):
        return self.request.query_params.get('lang', 'ru')


class NewsViewSet(viewsets.ModelViewSet, LanguageParamMixin):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsRegisteredUserOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsFilter
    search_fields = ['title', 'content',]


    @action(detail=True, methods=['POST'])
    def add_to_favorite(self, request, pk=None):
        instance = self.get_object()
        instance.is_favorite = True
        instance.save()
        return Response('Объект успешно добавлен в избранное!')

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        lang = self.get_language()

        instance.title = translator.translate(instance.title, dest=lang).text
        instance.content = translator.translate(instance.content, dest=lang).text

        serializer = self.get_serializer(instance)
        return Response(serializer.data)


